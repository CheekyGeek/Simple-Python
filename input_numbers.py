import os.path
from os import path
option = "Yes"
while (option == "Yes"):
    if (path.exists("numbers.txt")):
        f = open ("numbers.txt", "a")
        number = raw_input ("Please enter your desired input: ")
        if(number.isdigit()):
            f.write("This is the user input: " + number + "\n")
        else:
            print("You did not enter an integer! Please try again.")
    else:
        f = open ("numbers.txt", "w")
        number = raw_input ("Please enter your desired input: ")
        if(number.isdigit()):
            f.write("This is the user input: " + number + "\n")
        else:
            print("You did not enter an integer! Please try again.")
    option = raw_input ("Do you want to continue? Enter Yes to continue No to exit: ")
f.close()

    