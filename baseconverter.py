"""This is a base Calculator"""
#this converts all binary decimal octa and hex decimal between each other
#complexity expectation O(N).
#check validity of number
import os #os.system('cls||clear') #exitcode
import webbrowser
import random

urlwf = "https://c.tenor.com/rCJQJlAHsccAAAAd/avengers-wakanda-forever.gif"
new = 1
print("Hello!".center(149))
#First page of introduction and selection of Options
def baseselect():
    """This Function is used to select the initial Base Value."""
    print("\n")
    print(" Welcome to Base Converter. I can Convert Decimals, Binary and Hexadecimal Values into each other".center(149))
    print("Please select an option to continue-")
    print("Decimal to Binary (Press 1)".center(75) + "Binary to Decimal (Press 2)".center(75))
    print("Decimal to Hexadecimal (Press 3)".center(75) + "Hexadecimal to Decimal (Press 4)".center(75))
    print("Decimal to Octal (Press 5)".center(75) + "Octal to Decimal (Press 6)".center(75))
    while True:
        try:
            y = input("Enter your option:  ").lower()
            if y == "wakanda":
                easteregg()
            elif y == "time":
                time()
            elif y == "exit":
                exit()
            elif y == "no":
                print("Fine, I'll do it myself".center(149))
                y = random.randint(1,6)
                x = int(y)
                if x >= 7  or x <= 0:
                    print("Oops! That number isn't valid. Please enter a number between 1 and 6.")
                else:
                    break
            else:
                x = int(y)
                if x >= 7  or x <= 0:
                    print("Oops! That number isn't valid. Please enter a number between 1 and 6.")
                else:
                    break
        except ValueError:
            print("Oops! That isn't a number. Please enter a number between 1 and 4.")
    return x

#Decimal to Binary
def dectobin():
    """This function converts Decimal to Binary."""
    print("Welcome to Decimal to Binary Converter".center(149))
    while True:
        try:
            inp = int(input("Enter Decimal Value:  "),10)
            print("You entered",inp)
            break
        except ValueError:
            print("Oops! That number isn't valid. Please enter a decimal Value.".center(149))
    return bin(inp)
#Binary to Decimal
def bintodec():
    """This function converts Binary to Decimal."""
    print("Welcome to Bimary to Decimal Converter".center(149))
    while True:
        try:
            inp = input("Enter Binary Value:  ")
            binp = int(inp)
            print("You entered",binp)
            break
        except ValueError:
            print("Oops! That number isn't valid. Please enter a valid binary Value.".center(149))
            print("Remember a binary number consists only 0's and 1's".center(149))

    return int(inp,base=2)

def dectohex():
    """This function converts Decimal to Hexadecimal"""
    print("Welcome to Decimal to HexaDecimal Converter".center(149))
    while True:
        try:
            inp = int(input("Enter Decimal Value:  "))
            print("You entered",inp)
            break
        except ValueError:
            print("Oops! That number isn't valid. Please enter a valid decimal Value.".center(149))
            print("Remember a decimal number consists digits 0-9".center(149))

    return hex(inp)

def hextodec():
    """This converts Hexadecimal to Decimal"""
    print("Welcome to Hexadecimal to Decimal Converter".center(149))
    while True:
        try:
            inp = "0x" + input("Enter Hexadecimal Value:   ")
            print("You enterd", inp)
            break
        except ValueError:
            print("Oops! That value isn't valid. Please enter a valid Hexadecimal Value.".center(149))
            print("Remember a Hex number consists digits 0-9 and letter a-f".center(149))
    return int(inp,base=16)

def dectooct():
    """This converts Decimal Value to Octal Value"""
    print("Welcome to Decimal to Octal Converter".center(149))
    while True:
        try:
            inp = input("Enter Decimal Value:   ")
            print("You entered:",inp)
            break
        except ValueError:
            print("Oops! That value isn't valid. Please enter a valid Decimal Value.".center(149))
            print("Remember a Hex number consists digits 0-9".center(149))
    return oct(int(inp))

def octtodec():
    """This converts Octal Value to Decimal Value"""
    print("Welcome to Octal to Decimal Converter".center(149))
    while True:
        try:
            inp = "0o" + input("Enter Octal Value:   ")
            print("You enterd", inp)
            break
        except ValueError:
            print("Oops! That value isn't valid. Please enter a valid Octal Value.".center(149))
            print("Remember a Octal number consists digits 0-7".center(149))
    return int(inp,base=8)

def easteregg():
    webbrowser.open(urlwf,new=new)
def time():
    os.startfile("G:\Himanshu\Python Projects\Coursera Chuck 2\clock.py")

#FLOW
while True:
    bs = baseselect()
    if bs == 1:
        print("Corresponding Binary Number is", dectobin().replace("0b",""))
    elif bs == 2:
        print("Corresponding Decimal Number is", bintodec())
    elif bs == 3:
        print("Corresponding Hexadecimal Value is", dectohex().replace("0x",""))
    elif bs == 4:
        print("Corresponding Decimal Number is",hextodec())
    elif bs == 5:
        print("Corresponding Octal Number is", dectooct().replace("0o",""))
    elif bs == 6:
        print("Corresponding Decimal Number is",octtodec())