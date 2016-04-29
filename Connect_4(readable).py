import os
import time

board = []
player = "O"
aiCheck = ["","","","","","",""]

for x in range(6):
    board.append([" "]*7)
    
###################################Functions###################################
def printBoard(board):
    os.system("cls")
    print("  1   2   3   4   5   6   7 ")
    for row in range(6):
        print("| %s | %s | %s | %s | %s | %s | %s |\n-----------------------------" %(board[row][0],board[row][1],board[row][2],board[row][3],board[row][4],board[row][5],board[row][6]))
 
def animateMove(board, col, player):
    board[0][col] = player
    printBoard(board)
    time.sleep(.1)
    for check in range(1,6):
        if board[check][col] == " ":
            board[check - 1][col] = " "
            board[check][col] = player
            printBoard(board)
            time.sleep(.1)
        else:
            break
    else:
        return checkForWin(board, check, col, player)
    return checkForWin(board, check-1, col, player)
            
def checkForWin(board, row, col, player):
    colCheck = ""
    diagonalCheck = ""
    toCheck = player*4
    for checkCol in range(4):
        if board[row][checkCol:checkCol+4] == [player,player,player,player]:
            return True
    for checkRow in range(6):
        colCheck += board[checkRow][col]
    if toCheck in colCheck:
        return True
    #RLUD Diagonal:
    startRow = row + min(5-row,col)
    startCol = col - min(5-row,col)
    for x in range(min(startRow,6-startCol)+1):
        diagonalCheck += board[startRow - x][startCol + x]
    if toCheck in diagonalCheck:
        return True
    diagonalCheck = ""
    #LRUD Diagonal:
    startRow = row + min(5-row, 6-col)
    startCol = col + min(5-row, 6-col)
    for x in range(min(startRow, startCol)+1):
        diagonalCheck += board[startRow - x][startCol - x]
    if toCheck in diagonalCheck:
        return True    
    return False
 
#############################Run Game################################################################
printBoard(board)
while True:
    if ' ' not in board[0][0:7]:
        input("Draw! Press [Enter] to exit")
        break
    playerMove = input("Player %s, Make a move! "%(player))
    try:
        playerMove = int(playerMove)
        if playerMove >= 1 and playerMove <= 7:
            if board[0][playerMove-1] == " ":
                if animateMove(board, playerMove-1, player):
                    input("%s wins!! Press [Enter] to exit"%(player))
                    break
                if player == "O":
                    player = "X"
                else:
                    player = "O"
            else:
                print("Must choose a free column")
        else:
            print("Must be a number from 1-7") 
    except ValueError:
        print("Must be a number from 1-7")
