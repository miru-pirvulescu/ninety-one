import sys
from input_parser import InputParser
from utils import isValidFileType

class App:
    def getTopScorers(self, path):
        """
        Get the top scorers in a CSV file
        Params: 
            path: str - path to file containing data to process
        Return:
            topScorers: List[str] - list of all the participants who have the highest score
        """
        topScorers = []
        currentTopScore = -1 # Will assume a constraint that the scores cannot be below 0
        inputParser = InputParser(path, delimiter=",")

        for entry in inputParser.parseFile():
            if entry[1] > currentTopScore:
                currentTopScore = entry[1]
                topScorers = [entry[0]]
            elif entry[1] == currentTopScore:
                topScorers.append(entry[0])

        return sorted(topScorers), currentTopScore


    def run(self):
        path = input("Please send a file path: ")

        if not isValidFileType(path):
            sys.stdout.write("A file with a .csv or .txt extension is required!")
            return
            
        try:
            participants, topScore = self.getTopScorers(path)
            for p in participants:
                sys.stdout.write(p)
                sys.stdout.write('\n')
            sys.stdout.write("Score: %s" % str(topScore))
        except:
            sys.stdout.write("Provided path does not exist!")


def __main__():
    App().run()


if __name__ == "__main__":
    __main__()