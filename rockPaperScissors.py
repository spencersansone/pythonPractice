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

b = True
choicesArray = ["R","P","S"]

#ask user: rock paper scissors?

userChoice = input("Rock (R), paper (P) or scissors (S)?:").upper()

while(b):
    if userChoice.upper() not in choicesArray:
        userChoice = input("Please try again. Rock (R), paper (P) or scissors (S)?:")
    else:
       b = False

computerChoice = choicesArray[randint(0,2)]

result_string = result(userChoice,computerChoice)

print("""
User: {}
Computer: {}
Result: {}
""".format(userChoice.upper(),computerChoice,result_string))


    

#have computer pick rock paper or scissors

#determine who wins or if there is a draw

#print result (Rock vs Paper: User wins!)
