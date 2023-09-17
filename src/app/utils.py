import os.path

def getPathToTestData():
    my_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(my_path, "..\\..\\data\\TestData.csv")

def makeNameString(firstName: str, lastName: str):
    """
    Create name string for participant
    Params: 
        firstName: str
        lastName: str
    Return:
        A str of the two names formatted nicely
    """
    return "{fn} {ln}".format(fn = firstName, ln=lastName)