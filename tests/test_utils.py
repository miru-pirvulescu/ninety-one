from src.app.utils import isValidFileType, getPathToTestData, makeNameString
from unittest import TestCase

class UtilsTests(TestCase):
    def test_isValidFileType(self):
        self.assertTrue(isValidFileType("foo.csv"))
        self.assertFalse(isValidFileType("foo.bar"))

    def test_getPathToTestData(self):
        self.assertIn("\data\TestData.csv", getPathToTestData())

    def test_makeNameString(self):
        self.assertEqual(makeNameString("foo", "bar"), "foo bar")

    