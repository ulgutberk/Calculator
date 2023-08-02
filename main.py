# Get Username

def getName():
    userName = input("What is your name?: ")
    print(f"Welcome to our Calculator Program, {userName}. I hope you are doing well.")
    return userName


# Choose the calculation type
def calculatorSelect():
    print(f"{name}, choose the calculation you want to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    selection = input("Enter the number of your choice (1/2/3/4): ")
    if selection not in ['1', '2', '3', '4']:
        print("Make a valid choice")
        return calculatorSelect()
    else:
        return selection


def correctSelect(operationSelection):
    global correctSelectControl
    selectionList = ("Addition", "Subtraction", "Multiplication", "Division")
    if operationSelection == 1:
        print(f"Your selection is {selectionList[1]}")
        choice = str(input("Do you confirm your choice ? (Yes or Not):  "))
        if choice == "Yes" or choice == "YES" or choice == "yes":
            print(f"{selectionList[operationSelection]} selected")
            correctSelectControl = True
        else:
            print("!You did not confirm the selection, choose from the beginning!")
            calculatorSelect()
        return correctSelectControl

    elif operationSelection == 2:
        print(f"Your selection is {selectionList[2]}")
        choice = str(input("Do you confirm your choice ? (Yes or Not):  "))
        if choice == "Yes" or choice == "YES" or choice == "yes":
            print(f"{selectionList[operationSelection]} selected")
            correctSelectControl = True
        else:
            print("!You did not confirm the selection, choose from the beginning!")
            calculatorSelect()
        return correctSelectControl
    elif operationSelection == 3:
        print(f"Your selection is {selectionList[3]}")
        choice = str(input("Do you confirm your choice ? (Yes or Not):  "))
        if choice == "Yes" or choice == "YES" or choice == "yes":
            print(f"{selectionList[operationSelection]} selected")
            correctSelectControl = True
        else:
            print("!You did not confirm the selection, choose from the beginning!")
            calculatorSelect()
        return correctSelectControl
    elif operationSelection == 4:
        print(f"Your selection is {selectionList[4]}")
        choice = str(input("Do you confirm your choice ? (Yes or Not):  "))
        if choice == "Yes" or choice == "YES" or choice == "yes":
            print(f"{selectionList[operationSelection]} selected")
            correctSelectControl = True
        else:
            print("!You did not confirm the selection, choose from the beginning!")
            calculatorSelect()
        return correctSelectControl


# Get the Numbers
def getNumber():
    global num1
    global num2
    try:
        num1 = float(input("Enter the first number: "))

    except:
        print("Num1 is not valid. Please enter a valid number")
        return getNumber()
    try:
        num2 = float(input("Enter the second number: "))
    except:
        print("Num2 is not valid. Please enter a number")
        return getNumber()
    if operation == 1:
        print(f"The result is: {num1 + num2}")
    elif operation == 2:
        print(f"The result is: {num1 - num2}")
    elif operation == 3:
        print(f"The result is: {num1 * num2}")
    elif operation == 4:
        print(f"The result is: {num1 / num2}")


name = getName()
newCalculation = True
while newCalculation:
    correctSelectControl = False
    operation = int(calculatorSelect())
    while not correctSelectControl:
        correctSelect(operation)
    getNumber()
    keepCalculation = input("Do you want to make a new Calculation ?: ")
    if keepCalculation == "Yes" or keepCalculation == "YES" or keepCalculation == "yes":
        continue
    else:
        print("The program has completed its task, I wish you a good day")
        newCalculation = False
