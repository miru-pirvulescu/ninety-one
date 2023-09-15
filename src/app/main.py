import csv
import os.path
import sys

def _getPathToTestData():
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


def getTopScorers(scoreData: csv):
    """
    Get the top scorers in a CSV file
    Params: 
        scoreData: csv - file containing the name and score of the given participants
    Return:
        topScorers: List[str] - list of all the participants who have the highest score
    """
    topScorers = []
    currentTopScore = -1 # Will assume a constraint that the scores cannot be below 0
    data = csv.reader(scoreData, delimiter=',')
    next(data, None) # Skip the header
    for row in data:
        if int(row[2]) > currentTopScore:
            currentTopScore = int(row[2])
            topScorers = [makeNameString(row[0], row[1])]
        elif int(row[2]) == currentTopScore:
            topScorers.append(makeNameString(row[0], row[1]))

    return sorted(topScorers), currentTopScore


def __main__():
    path = input("Please send a file path: ")

    if path[-4:] != ".csv": # Check that the extension of the file is supported
        sys.stdout.write("A file with a .csv extension is required!")
        return
        
    try:
        with open(path) as testData:
            participants, topScore = getTopScorers(testData)
            for p in participants:
                sys.stdout.write(p)
                sys.stdout.write('\n')
            sys.stdout.write("Score: %s" % str(topScore))
    except:
        sys.stdout.write("Provided path does not exist!")


if __name__ == "__main__":
    __main__()