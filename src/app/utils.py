import os.path
import sys

HELP_TEXT = """Commands:
    - example: see the top scorers from the test data
    - help: see command list
    - run: process results for participants from .csv or .txt file
    - quit: leave app
"""

def isValidFileType(path):
    """Ensure the file type is supported by the app."""
    extension = path[-4:]
    return extension in [".csv", ".txt"]

def getHelpText():
    sys.stdout.write(HELP_TEXT)

def getPathToTestCSV():
    my_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(my_path, "..\\..\\data\\TestData.csv")

def getPathToTestTXT():
    my_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(my_path, "..\\..\\data\\TestData.txt")

def makeNameString(firstName, lastName):
    """
    Create name string for participant
    Params: 
        firstName: str
        lastName: str
    Return:
        A str of the two names formatted nicely
    """
    return "{fn} {ln}".format(fn = firstName, ln=lastName)

