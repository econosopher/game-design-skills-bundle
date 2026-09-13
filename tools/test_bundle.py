"""Offline regression tests: python3 -m unittest discover -s tools -p 'test_*.py'."""
import builtins
import contextlib
import importlib.util
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

import bundle


class PackagingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / 'sample'
        self.skill.mkdir()
        (self.skill / 'SKILL.md').write_text('---\nname: sample\ndescription: Analyze a sample.\n---\n# Sample\n')

    def run_cli(self, action):
        return subprocess.run([sys.executable, str(Path(bundle.__file__)), action,
                               '--root', str(self.root)], capture_output=True, text=True)

    def test_reproducible_build_and_source_drift(self):
        self.assertEqual(self.run_cli('build').returncode, 0)
        archive = self.root / 'package-skills/sample.skill'
        first = archive.read_bytes()
        self.assertEqual(self.run_cli('build').returncode, 0)
        self.assertEqual(first, archive.read_bytes())
        (self.skill / 'SKILL.md').write_text((self.skill / 'SKILL.md').read_text() + 'Changed.\n')
        result = self.run_cli('check')
        self.assertEqual(result.returncode, 1)
        self.assertIn('Archive/source mismatch', result.stdout)

    def test_missing_reference(self):
        with (self.skill / 'SKILL.md').open('a') as stream:
            stream.write('[Guide](references/missing.md)\n')
        self.assertIn('missing Markdown link', bundle.inspect_skill(self.skill)[0])
        self.assertEqual(self.run_cli('build').returncode, 1)
        self.assertFalse((self.root / 'package-skills/sample.skill').exists())

    def test_symlink_rejected(self):
        (self.skill / 'linked').symlink_to(self.skill / 'SKILL.md')
        with self.assertRaisesRegex(ValueError, 'Symlink'):
            bundle.members(self.skill)

    def test_unsafe_and_duplicate_archive_paths(self):
        self.assertEqual(self.run_cli('build').returncode, 0)
        archive = self.root / 'package-skills/sample.skill'
        with zipfile.ZipFile(archive, 'a') as z:
            z.writestr('../escape', b'bad')
            with self.assertWarns(UserWarning):
                z.writestr('../escape', b'bad')
        result = self.run_cli('check')
        self.assertEqual(result.returncode, 1)
        self.assertIn('Unsafe archive path', result.stdout)
        self.assertIn('Duplicate archive paths', result.stdout)

    def test_cache_excluded(self):
        cache = self.skill / '__pycache__'
        cache.mkdir()
        (cache / 'artifact.pyc').write_bytes(b'cache')
        self.assertEqual(set(bundle.members(self.skill)), {'sample/SKILL.md'})


class RendererDependenciesTests(unittest.TestCase):
    def test_missing_playwright_never_installs_or_launches(self):
        path = Path(__file__).resolve().parents[1] / 'moodboard-generator/scripts/render_png.py'
        spec = importlib.util.spec_from_file_location('renderer', path)
        renderer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(renderer)
        original_import = builtins.__import__

        def missing_playwright(name, *args, **kwargs):
            if name.startswith('playwright'):
                raise ImportError('deliberately absent in test')
            return original_import(name, *args, **kwargs)

        stderr = io.StringIO()
        with patch('builtins.__import__', side_effect=missing_playwright), \
                patch.object(renderer.subprocess, 'run') as run, \
                contextlib.redirect_stderr(stderr):
            self.assertFalse(renderer.try_playwright('missing.html', 'missing.png', 800))
            run.assert_not_called()
        self.assertIn('dedicated environment', stderr.getvalue())


if __name__ == '__main__':
    unittest.main()
