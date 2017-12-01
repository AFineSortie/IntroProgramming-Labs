# Author: Chris Petrucelli
# 03/11/2017
# Artificial Personality

from graphics import *

#def intro():
#    print("\nHey there, my name is Boigis")
    # Tell the user what to input
#    print("\nYou can interact with me in a few ways, with the commands, 'reward', 'punish', 'threaten', and 'joke'.")

def lookup(matrix, currEmot, app, inputBox):
    while app.getKey() != "Return": pass
    cmd = str(inputBox.getText()).lower()
    if cmd == "reward":
        cmd = 0
        Text(Point(5,3), "it work").draw(app)
    elif cmd == "punish":
        cmd = 1
    elif cmd == "threaten":
        cmd = 2
    elif cmd == "joke":
        cmd = 3
    newEmot = matrix[currEmot][cmd]
    #print(matrix[currEmot])
    currEmot = newEmot
   # print(currEmot)
   # print(cmd)
    return currEmot

def response(currEmot):
    if currEmot == 0:
        print("\nI hate you!")
    elif currEmot == 1:
        print("\nYou're awful...")
    elif currEmot == 2:
        print("\nYou're scaring me!")
    elif currEmot == 3:
        print("\nYou're the best!")
    elif currEmot == 4:
        print("\nThat's not very nice...")
    elif currEmot == 5:
        print("\nI wasn't expecting that!")
    return currEmot




   
def main():

    app = GraphWin("Artificial Personality", 500, 300)
    app.setCoords(0, 0, 10, 10)

    Text(Point(5,8), "Hey there, my name is Boigis!").draw(app)
    Text(Point(5,6), "You can interact with me in a few ways").draw(app)
    Text(Point(5,5), "Using 'reward', 'punish', 'threaten', and 'joke'").draw(app)


    inputBox = Entry(Point(2,3), 8)
    inputBox.draw(app)


    #Rows
    anger = 0
    disgust = 1
    fear = 2
    happiness = 3
    sadness = 4
    surprise = 5

    #Columns
    reward = 0
    punish = 1
    threaten = 2
    joke = 3
    
    matrix = [
        [3, 4, 0, 3],
        [5, 4, 0, 5],
        [5, 1, 0, 5],
        [3, 1, 2, 3],
        [3, 1, 2, 5],
        [3, 1, 2, 3]]

    currEmot = 3

    while True:
        currEmot = response(lookup(matrix, currEmot, app, inputBox))
    
main()
