#Arithmetic Engine
import math
#Show Intro
def intro():
    print("This is the Arithmetic Engine. This program accepts a user command (add, mult, diff, quot, quit) and two numbers and calculates the correct command with those given numbers")

#Loop
def engine():
    while True:
        cmd = input("Enter the desired command: ").lower()
        if cmd == "quit":
            break

        try:
           num1 = int(input("Enter the first number: "))
           num2 = int(input("Enter the second number: "))
        except:
            print("You must enter a valid number")
            continue

        answer = 0
        if cmd == "add":
            answer = num1 + num2
            print(answer)
        elif cmd == "mult":
            answer = num1 * num2
            print(answer)
        elif cmd == "diff":
            answer = num1 - num2
            print(answer)
        elif cmd == "quot":
            answer = num1 / num2
            print(answer)
        else:
            print("That was not a valid command!")
            quit()

def end():
    print("Thanks for stoppin' by!")



def main():
    intro()
    engine()
    end()


main()
