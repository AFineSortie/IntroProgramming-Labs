#CMPT 120 Intro to Programming
#Lab #7
#Author: Christopher Petrucelli
#Created 2017-10-27
symbol = [ " ", "x", "o" ]

def printRow(row):
    #initialize output to the left border
    output = "| "
    #for each square in the row...
    for square in row:
        #add to output the symbol for this square followed by a border
        output = output + symbol[square] + " | "
    #print the completed output for this row
    print(output)

def printBoard(board):
    border = "+---+---+---+"
    #print the top border
    print(border)
    #for each row in the board...
    for row in board:
        #print the row
        printRow(row)
        #print the next border
        print(border)
    

def markBoard(board, row, col, player):
    #check to see whether the desired square is blank
    if board[row][col] == 0:
        board[row][col] = player
        #if so, set it to the player number

def getPlayerMove():
    row = int(input("Enter the row number for your move: ")) #prompt the user seperately for the row and column numbers
    col = int(input("Enter the column number for your move: "))
    return (row - 1,col - 1) #then return that row and column instead of (0,0)

def hasBlanks(board):
    #for each row in the board...
    for row in board:
        #for each square in the row...
        for square in row:
            #check whether the square is blank
            if square == 0:
                return True
                #if so, return True
    return False
                #if no square is blank, return false

def checkWin(board):
    for row in board:
        if row == [1, 1, 1]:
            print("Player 1 Wins!")
            return False
        elif row == [2, 2, 2]:
            print("Player 2 Wins!")
            return False
    if board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1:
        print("Player 1 Wins")
        return False
    elif board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2:
        print("Player 2 Wins")
        return False
    return True

def main():
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    player = 1
    while checkWin(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board, row, col, player)
        player = player % 2 + 1 #switch player for next turn
    printBoard(board)
main()
