# Author: Chris Petrucelli
# 03/11/2017
# Artificial Personality

from graphics import *

def lookup(matrix, currEmot, app, inputBox):
    global output
    while app.getKey() != "Return": pass
    cmd = str(inputBox.getText()).lower()
    inputBox.setText("")
    if cmd == "reward":
        cmd = 0
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

def response(app, currEmot):
    global output
    output.setText("")
    if currEmot == 0:
        output = Text(Point(6,3), "I hate you!").draw(app)
    elif currEmot == 1:
        output = Text(Point(6,3), "You're awful...").draw(app)
    elif currEmot == 2:
        output = Text(Point(6,3), "You're scaring me!").draw(app)
    elif currEmot == 3:
        output = Text(Point(6,3), "You're the best!").draw(app)
    elif currEmot == 4:
        output = Text(Point(6,3), "That's not very nice...").draw(app)
    elif currEmot == 5:
        output = Text(Point(6,3), "I wasn't expecting that!").draw(app)

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
    global output
    output = Text(Point(6,3), "").draw(app)

    while True:
        currEmot = response(app, lookup(matrix, currEmot, app, inputBox))
    
main()
