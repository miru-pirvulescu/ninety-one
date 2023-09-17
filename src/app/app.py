import sys

from input_parser import InputParser
from utils import isValidFileType, getHelpText, getPathToTestCSV

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

    def processCommand(self, command):
        """
        Based on the available commands, provide the appropriate answer.
        Params:
            - command: str - a command coming from the user
        """
        if command.lower() == "help":
            getHelpText()

        elif command.lower() == "example":
            sys.stdout.write("Procesing results from %s \n" % getPathToTestCSV())
            participants, score = self.getTopScorers(getPathToTestCSV())
            self.sendResults(participants, score)

        elif command.lower() == "run":
            self.run()

        elif command.lower() == "quit":
            sys.stdout.write("Goodbye!")
            return
        else:
            sys.stdout.write("I'm afraid I don't understand that command. Please type 'help' to see what I understand")

        newCommand = input("\nWhat else can I help with? ")
        self.processCommand(newCommand)


    def run(self):
        """Run the code to calculate top scorers"""
        path = input("Please send a file path: ")

        if not isValidFileType(path):
            sys.stdout.write("A file with a .csv or .txt extension is required!")
            return
        try:
            participants, score = self.getTopScorers(path)
            self.sendResults(participants, score)
        except:
            sys.stdout.write("Provided path does not exist!")
    

    def sendResults(self, participants, topScore):
        """Display the results to the users"""
        for p in participants:
            sys.stdout.write(p)
            sys.stdout.write('\n')
        sys.stdout.write("Score: %s" % str(topScore))