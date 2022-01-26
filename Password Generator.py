import random

def weak(): #mixture of numbers and lower case letters
    charset = "abcdefghijklmnopqrstuvwxyz"
    length = random.randint(5,10)
    password = []
    
    for i in range (0,length):
        x = random.randint(1,2)
        if x == 1:
            case = random.randint(0,25)
            char = charset[(int(case))]
            password.append(char)
        elif x == 2:
            char = random.randint(0,9)
            password.append(char)

    string = ""
    for i in password:
        string = string + str(i)
    print(string)


def medium(): #mixture of numbers, lower/upper case letters
    charLOW = "abcdefghijklmnopqrstuvwxyz"
    charUP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    length = random.randint(10,15)
    password = []

    for i in range (0,length):
        x = random.randint(1,3)
        if x == 1:
            case = random.randint(0,25)
            char = charLOW[(int(case))]
            password.append(char)
        elif x == 2:
            char = random.randint(0,9)
            password.append(char)
        elif x == 3:
            case = random.randint(0,25)
            char = charUP[(int(case))]
            password.append(char)

    string = ""
    for i in password:
        string = string + str(i)
    print(string)


def secure(): #mixture of numbers, lower/upper case letters, symbols
    charLOW = "abcdefghijklmnopqrstuvwxyz"
    charUP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    charSYM = "!£$%^&*()_+-={}[]|\<,>.?/@'~#¬`"
    length = random.randint(15,20)
    password = []

    for i in range (0,length):
        x = random.randint(1,4)
        if x == 1:
            case = random.randint(0,25)
            char = charLOW[(int(case))]
            password.append(char)
        elif x == 2:
            char = random.randint(0,9)
            password.append(char)
        elif x == 3:
            case = random.randint(0,25)
            char = charUP[(int(case))]
            password.append(char)
        elif x == 4:
            case = random.randint(0,30)
            char = charSYM[(int(case))]
            password.append(char)

    string = ""
    for i in password:
        string = string + str(i)
    print(string)


def menu():
    print("Welcome to the Password Generator")
    print("")
    print("You can change your password at a later date")
    print("")
    print("1 - Weak")
    print("2 - Medium")
    print("3 - Secure")
    print("")

    choice = input("Choose a password strength: ")

    if choice == "1":
        weak()
    elif choice == "2":
        medium()
    elif choice == "3":
        secure()


menu()

