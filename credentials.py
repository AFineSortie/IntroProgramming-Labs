# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Christopher Petrucelli
# Created: 2017-09-29
first = "John"
last = "Doe"
uname = "smitty.warbenjagermanjenson"
passwd = "uhhh"

def name():
    # get user's first and last names
    global first
    global last
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    fullname = [first, last]
    return fullname

def uname(names):
    global uname
    uname = names[0] + "." + names[1]
    # testing print(uname)
    
    # ask user to create a new password

def password():
    global passwd
    passwd = input("Create a new password: ")
    while True:
        if len(passwd) < 8:
            print("Fool of a Took! That password is feeble!")
            passwd = input("Create a new password: ")
        else:
            print("The force is strong in this one…")
            print("Account configured. Your new email address is",
            uname + "@marist.edu")
            break
        
def main():
    names = name()
    uname(names)
    password()

main()
