from app import App

def __main__():
    firstCommand = input("Welcome! What would you like to begin with? (type help if you are unsure): ")
    App().processCommand(firstCommand)

if __name__ == "__main__":
    __main__()