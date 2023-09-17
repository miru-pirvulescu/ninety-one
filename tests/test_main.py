from unittest.mock import patch
from src.app.main import App
from src.app.utils import getPathToTestData
from unittest import TestCase

import contextlib
import io

class AppTests(TestCase):
    def setUp(self):
        self.app = App()

    def test_getTopScorers(self):
        names, score = self.app.getTopScorers(getPathToTestData())
        self.assertListEqual(names, ["George Of The Jungle", "Sipho Lolo"])
        self.assertEqual(score, 78)

    @patch('builtins.input', return_value=getPathToTestData())
    def test_run(self, mockInput):
        with io.StringIO() as buf:
            with contextlib.redirect_stdout(buf):
                self.app.run()
                self.assertEqual(buf.getvalue(), "George Of The Jungle\nSipho Lolo\nScore: 78")

    @patch('builtins.input', return_value="test.xlsx")
    def test_run_wrong_file_type(self, mockInput):
        with io.StringIO() as buf:
            with contextlib.redirect_stdout(buf):
                self.app.run()
                self.assertEqual(buf.getvalue(), "A file with a .csv extension is required!")

    @patch('builtins.input', return_value="fooBar.csv")
    def test_run_fileNotFound(self, mockInput):
        with io.StringIO() as buf:
            with contextlib.redirect_stdout(buf):
                self.app.run()
                self.assertEqual(buf.getvalue(), "Provided path does not exist!")