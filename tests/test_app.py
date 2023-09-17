from unittest.mock import patch
from src.app.main import App
from src.app.utils import getPathToTestCSV, getPathToTestTXT, HELP_TEXT
from unittest import TestCase

import contextlib
import io

class AppTests(TestCase):
    def setUp(self):
        self.app = App()

    def test_getTopScorers(self):
        names, score = self.app.getTopScorers(getPathToTestCSV())
        self.assertListEqual(names, ["George Of The Jungle", "Sipho Lolo"])
        self.assertEqual(score, 78)

    @patch('builtins.input', return_value="quit")
    def test_processCommand_help(self, mockInput):
        with io.StringIO() as buf:
            with contextlib.redirect_stdout(buf):
                self.app.processCommand("help")
                self.assertEqual(buf.getvalue(), HELP_TEXT + "Goodbye!")

    @patch('builtins.input', return_value="quit")
    def test_processCommand_example(self, mockInput):
        with io.StringIO() as buf:
            with contextlib.redirect_stdout(buf):
                self.app.processCommand("example")
                self.assertEqual(buf.getvalue(), 'Procesing results from c:\\Users\\mirun\\Desktop\\Projects\\NinetyOne\\ninety-one\\src\\app\\..\\..\\data\\TestData.csv \nGeorge Of The Jungle\nSipho Lolo\nScore: 78Goodbye!')

    @patch('builtins.input', side_effect = [getPathToTestTXT(), "quit"])
    def test_processCommand_run(self, mockInput):
        with io.StringIO() as buf:
            with contextlib.redirect_stdout(buf):
                self.app.processCommand("run")
                self.assertEqual(buf.getvalue(), "Bruce Wayne\nJack White\nScore: 97Goodbye!")

    def test_processCommand_quit(self):
        with io.StringIO() as buf:
            with contextlib.redirect_stdout(buf):
                self.app.processCommand("quit")
                self.assertEqual(buf.getvalue(), "Goodbye!")

    @patch('builtins.input', return_value=getPathToTestCSV())
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
                self.assertEqual(buf.getvalue(), "A file with a .csv or .txt extension is required!")

    @patch('builtins.input', return_value="fooBar.csv")
    def test_run_fileNotFound(self, mockInput):
        with io.StringIO() as buf:
            with contextlib.redirect_stdout(buf):
                self.app.run()
                self.assertEqual(buf.getvalue(), "Provided path does not exist!")

    def test_sendResults(self):
        participants=["foo", "bar"]
        score=100
        with io.StringIO() as buf:
            with contextlib.redirect_stdout(buf):
                self.app.sendResults(participants, score)
                self.assertEqual(buf.getvalue(), "foo\nbar\nScore: 100")