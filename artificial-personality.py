# Author: Chris Petrucelli
# 03/11/2017
# Artificial Personality
def intro():
    print("\nHey there, my name is boigis")
    # Tell the user what to input
    print("\nYou can interact with me in a few ways, with the commands, 'reward', 'punish', 'threaten', and 'joke'.")

def lookup(matrix, currEmot):
    cmd = input("\nEnter a command: ").lower()
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
    intro()

    while True:
        currEmot = response(lookup(matrix, currEmot))
    
main()
