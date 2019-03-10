# Author:   Isaiah Edwards
# Date:     03/09/2019
# Purpose:  Program to create codenames for projects; pulls in various names from files

# Imports random library for later use
import random

# Filenames
CONST_SCIFI = 'scifi.txt'
CONST_MYSTERIOUS = 'mysterious.txt'
CONST_GENERIC = 'generic.txt'

# An array of file names
FILES = [CONST_GENERIC, CONST_SCIFI, CONST_MYSTERIOUS]

# Method to get/verify user input, accepts values to define the range
# of choices the calling method allows
def getInput(rangeLow, rangeHigh):
    badInput = True
    choice = 0
    # Loop continues until badInput is changed by receiving
    # input between the accepted values
    while(badInput):
        try:
            choice = int(input("Enter a value for your choice: "))
            if choice >= rangeLow and choice <= rangeHigh:
                badInput = False # Executes only if input is numeric, and within appropriate range
            else:
                # This executes if the input is numeric, but outside of the desired range
                print("Enter a number between " + str(rangeLow) + " and " + str(rangeHigh))
        except:
            # This executes if the input cannot be converted to an integer
            print("Enter a numeric value between " + str(rangeLow) + " and " + str(rangeHigh))

    return choice

# Method to print menu
def printMenu():
    print("Menu:\n")
    print("1) Generate Code Name\n2) View Documentation\n3) Update Vocabulary Lists\n4) Exit\n")
    choice = getInput(1, 4)
    return choice

# Method to get random filename
def randomFile():
    # Generates random number in range of the files array indexes
    num = random.randint(0, 2)
    # Array of file names
    return FILES[num]

# Method to get random value from file, accepts previously determined file name
def randomValue(fileName):
    file = open(fileName, 'r')
    names = []
    numLines = 0
    # Counts lines in file, to be used for random number generation
    for line in file:
        names.append(line)

    file.close()
    return names[random.randint(0, len(names)-1)]

# Method to generate code names
def generateName():
    print("Types of code names: \n")
    print("1) Random\n2) Sci-Fi\n3) Mysterious\n4) Generic\n")
    choice = getInput(1, 4)
    # Array to hold two pieces of final code name
    names = ['', '']
    # Loops twice, gets a random value according to the type of
    # code name chosen by the user, then sets that value to either
    # position 0 or 1 of the "names" array
    for i in range(0, 2):
        if choice == 1:
            fileName = randomFile()
            names[i] = randomValue(fileName)
        elif choice == 2:
            names[i] = randomValue(CONST_SCIFI)
        elif choice == 3:
            names[i] = randomValue(CONST_MYSTERIOUS)
        else:
            names[i] = randomValue(CONST_GENERIC)

    # The two values in the names array are concatenated and returned
    # as a single string.  the .strip() method removes the newline character
    # from the end of the first array position, or first name in the final code name
    return names[0].strip() + " " + names[1]


# Method to display docs
def displayDocs():
    print("Docs:\nVersion: 1.0.0\n-------------------------\n")
    print("Overview\nCodeNames is a python command-line application to create project code names.\n\n")
    print("Usage\nCodeNames allows two basic actions: either generating a project name, or updating the wordlists\n"+
          "used to create the code names.  In essence, the application pulls two random strings from resource files\n"+
          "and puts them together to form a project code name.\n"+
          "The wordlists which the application pulls from are stored in three .txt files by default.  These files can\n"+
          "be updated through the other main command.  As of this version, only appending to the file is supported.\n"+
          "Contributions are welcome, view the github @ https://github.com/EdwardsIs/codenames")


# Method to update vocabulary
def updateVocabulary():
    print("Choose a list to update:\n")
    count = 1
    for file in FILES:
        print(str(count) + " " + file)
        count += 1
    # File to modify set to user input - 1, (because arrays start at 0. ;))
    # Opening with method 'append'
    fileChoice = open(FILES[getInput(1, count)-1], 'a')
    enterAnother = True
    while(enterAnother):
        val = input("Enter your addition: ")
        fileChoice.write(val)
        cont = input("Would you like to add another? Y/N: ")
        if cont == 'Y' or cont == 'y':
            continue
        elif cont == 'N' or cont == 'n':
            enterAnother = False
        else:
            print("Choice invalid; exiting maintenance menu")

    # Closing active file
    fileChoice.close()
            

def main():
    print('Welcome to CodeNames!')
    while(True):
        choice = printMenu()
        if choice == 1:
            # Generate code name
            codeName = generateName()
            print("Code name:\n----------------------------\n")
            print("Project " + codeName + "----------------------------\n")
        elif choice == 2:
            # View docs
            displayDocs()
        elif choice == 3:
            # Update vocabulary
            updateVocabulary()
        else:
            # Exit program
            exit()


main()
