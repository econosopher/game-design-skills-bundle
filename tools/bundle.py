#!/usr/bin/env python3
"""Build/check deterministic .skill archives against their skill source folders.

Usage: python3 tools/bundle.py check|build [--root PATH] [--skill NAME]
Uses only the Python standard library. No network or installation side effects.
"""
import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse
import zipfile

IGNORED = {'.DS_Store', '__pycache__', '.pytest_cache', '.git'}

def members(folder):
    result = {}
    for path in sorted(folder.rglob('*')):
        if any(part in IGNORED for part in path.relative_to(folder).parts):
            continue
        if path.is_symlink():
            raise ValueError(f'Symlink is not portable: {path}')
        if path.is_file() and path.suffix not in {'.pyc', '.pyo'}:
            result[f'{folder.name}/{path.relative_to(folder).as_posix()}'] = path.read_bytes()
    return result

def archive_bytes(files):
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=(2020, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    return stream.getvalue()

def inspect_skill(folder):
    errors = []
    text = (folder / 'SKILL.md').read_text()
    fm = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not fm:
        return ['Missing frontmatter']
    for key in ('name', 'description'):
        match = re.search(r'^' + key + r':\s*(.+)$', fm[1], re.M)
        if not match:
            errors.append(f'Missing {key}')
        elif key == 'name' and match[1].strip('"\'') != folder.name:
            errors.append('Skill name differs from directory')
    for path in folder.rglob('*.md'):
        if any(part in IGNORED for part in path.parts):
            continue
        content = path.read_text()
        for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', content):
            target = target.strip('<>')
            if urlparse(target).scheme or target.startswith('#'):
                continue
            dest = unquote(target.split('#')[0])
            if dest and not (path.parent / dest).exists():
                errors.append(f'{path.relative_to(folder)}: missing Markdown link {dest}')
        # Backticked resource paths are common in upstream skills. Generated output paths
        # and shell placeholders are intentionally not treated as source references.
        for target in re.findall(r'`((?:references|scripts|assets)/[A-Za-z0-9_./-]+\.[A-Za-z0-9]+)`', content):
            if not (folder / target).exists():
                errors.append(f'{path.relative_to(folder)}: missing resource {target}')
        if path.name == 'detailed-guide.md':
            for target in re.findall(r'`([A-Za-z0-9_-]+\.(?:md|json|pdf))`', content):
                # Known generated output filenames are not input references.
                if target in {'manifest.json','candidate_manifest.json','board.json','curation-notes.md'}:
                    continue
                if not (path.parent / target).exists() and not (folder / target).exists():
                    errors.append(f'{path.relative_to(folder)}: unresolved relative resource {target}')
    return errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['check', 'build'])
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--skill')
    args = parser.parse_args()
    root = args.root.resolve()
    folders = sorted(p.parent for p in root.glob('*/SKILL.md'))
    if args.skill:
        folders = [p for p in folders if p.name == args.skill]
    if not folders:
        parser.error('No matching skills')
    rows = []
    for folder in folders:
        errors = inspect_skill(folder)
        payload = members(folder)
        archive = root / 'package-skills' / f'{folder.name}.skill'
        if args.action == 'build' and not errors:
            archive.parent.mkdir(exist_ok=True)
            archive.write_bytes(archive_bytes(payload))
        if not archive.exists():
            errors.append('Missing packaged archive')
        else:
            try:
                with zipfile.ZipFile(archive) as z:
                    names = z.namelist()
                    stored = {n:z.read(n) for n in names if not n.endswith('/')}
                    if len(names) != len(set(names)):
                        errors.append('Duplicate archive paths')
                    if stored != payload:
                        errors.append('Archive/source mismatch')
                    if any(n.startswith('/') or '..' in Path(n).parts for n in names):
                        errors.append('Unsafe archive path')
            except zipfile.BadZipFile:
                errors.append('Invalid zip archive')
        rows.append({'skill':folder.name,'files':len(payload),'errors':errors,
                     'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest() if archive.exists() else None})
    print(json.dumps({'skills':len(rows),'passed':sum(not r['errors'] for r in rows),'results':rows},indent=2))
    return int(any(r['errors'] for r in rows))

if __name__ == '__main__':
    sys.exit(main())
