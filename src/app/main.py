import csv
import sys
from src.app.utils import makeNameString

class App():
    def getTopScorers(self, scoreData: csv):
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


    def run(self):
        path = input("Please send a file path: ")

        if path[-4:] != ".csv": # Check that the extension of the file is supported
            sys.stdout.write("A file with a .csv extension is required!")
            return
            
        try:
            with open(path) as data:
                participants, topScore = self.getTopScorers(data)
                for p in participants:
                    sys.stdout.write(p)
                    sys.stdout.write('\n')
                sys.stdout.write("Score: %s" % str(topScore))
        except:
            sys.stdout.write("Provided path does not exist!")


def __main__():
    app = App()
    app.run()

if __name__ == "__main__":
    __main__()