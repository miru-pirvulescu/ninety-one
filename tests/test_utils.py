from src.app.utils import isValidFileType, getPathToTestCSV, getPathToTestTXT, makeNameString
from unittest import TestCase

class UtilsTests(TestCase):
    def test_isValidFileType(self):
        self.assertTrue(isValidFileType("foo.csv"))
        self.assertFalse(isValidFileType("foo.bar"))

    def test_getPathToTestCSV(self):
        self.assertIn("\data\TestData.csv", getPathToTestCSV())

    def test_getPathToTestTXT(self):
        self.assertIn("\data\TestData.txt", getPathToTestTXT())

    def test_makeNameString(self):
        self.assertEqual(makeNameString("foo", "bar"), "foo bar")

    