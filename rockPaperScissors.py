from random import randint

def result(userChoice,computerChoice):
    if userChoice == computerChoice:
        return "It's a tie!"
    elif userChoice == "R":
        if computerChoice == "P":
            return "Computer wins!"
        else:
            return "User wins!"
    elif userChoice == "P":
        if computerChoice == "S":
            return "Computer wins!"
        else:
            return "User wins!"
    elif userChoice == "S":
        if computerChoice == "R":
            return "Computer wins!"
        else:
            return "User wins!"

keepGoing = True

while(keepGoing):
    b = True
    choicesArray = ["R","P","S"]

    

    while(b):
        userChoice = input("Rock, paper or scissors? (R/P/S):").upper()
        if userChoice.upper() not in choicesArray:
            print("Please try again")
        else:
           break

    computerChoice = choicesArray[randint(0,2)]

    r_string = result(userChoice,computerChoice)

    print("""
    User: {}
    Computer: {}
    Result: {}
    """.format(userChoice.upper(),computerChoice,r_string))

    while(True):
        playAgain = input("Would you like to play again? (y/n):")
        if playAgain == "n":
            keepGoing = False
            break
        elif playAgain == "y":
            break
        else:
            print("Please try again")
        
            
        
