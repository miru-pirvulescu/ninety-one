import os.path

def isValidFileType(path):
    """Ensure the file type is supported by the app."""
    return path[-4:] == ".csv"

def getPathToTestData():
    my_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(my_path, "..\\..\\data\\TestData.csv")

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

