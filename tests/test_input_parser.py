from src.app.input_parser import InputParser
from src.app.utils import getPathToTestCSV
from unittest import TestCase

class InputParserTests(TestCase):
    def setUp(self):
        self.parser = InputParser(getPathToTestCSV(), delimiter=",")

    def test_parseFile(self):
        expectedData = [
            ["Dee Moore", 56],
            ["Sipho Lolo", 78],
            ["Noosrat Hoosain", 64],
            ["George Of The Jungle", 78]
        ]
        self.assertListEqual(self.parser.parseFile(), expectedData)
