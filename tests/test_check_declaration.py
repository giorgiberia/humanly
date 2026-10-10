import contextlib
import io
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_declaration import check

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = (ROOT / "assets/HUMANLY-template.md").read_text()

class CheckDeclarationTests(unittest.TestCase):
    def call(self, data, strict=False):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            if data is not None:
                (root / "HUMANLY.md").write_text(data)
            with contextlib.redirect_stdout(io.StringIO()):
                return check(root, strict)

    def test_unassessed_template(self):
        self.assertEqual(self.call(TEMPLATE), 0)
        self.assertEqual(self.call(TEMPLATE, strict=True), 1)

    def test_H2_requires_all_lower_checks(self):
        data = TEMPLATE.replace('"unassessed"', '"H2"').replace('- [ ]', '- [x]')
        self.assertEqual(self.call(data), 0)
        bad = data.replace('- [x] Core tasks work', '- [ ] Core tasks work')
        self.assertEqual(self.call(bad), 1)

    def test_invalid_level(self):
        self.assertEqual(self.call(TEMPLATE.replace('"unassessed"', '"H4"')), 1)

    def test_missing(self):
        self.assertEqual(self.call(None), 2)

if __name__ == '__main__':
    unittest.main()
