# Get the top scorers
As part of my take-at-home task, I created a Python project that allows users to find out who are the top scoring participants in a test. The user needs to provide a path to the location of the file containing the names and scores of the participants, separated by comma into first name, last name, and score.

### Assumptions
- script should run from a Windows machine with Python 3 installed
- participants have scores greater than on equal to 0
- by default, the score files contain headers and the values are comma-separated (however the implemented parser allows for flexibility on this matter)
  
### Considerations
In order to outline the thinking process in the application, the identified sub-problems of the challenge have been assigned as issues in [this project](https://github.com/users/miru-pirvulescu/projects/1).

Given the requirement to make the app manageable and ready to evolve, the structure of the project has been made class-based. This would make new features easier to implement, for example adding a UI or enriching the capabilities of the file parser.

#### Input Parser
This small class processes the files at the specified location in the system, allowing for customisation of the value separator and for skipping an existent header.

#### App
This is where all the post-processing happens. The app has the algorithm to identify the top scorers in O(n) where n is the number of participants. It also processes the commands given by the users sent through the CLI.

### How to use
Running main.py will open a command prompt that takes the user into the application. With the help of the available commands, the user can perform the following actions:
  - example: see the top scorers from the test data
  - help: see command list
  - run: process results for participants from .csv or .txt file
  - quit: leave app
    
The run command will prompt the user to send a file path to the script. This file path must be an absolute path in the system.
