import random

board = [None] * 9
boardOrder = [None] * 9
x = set()
o = set()
winningBoards = [{0,1,2}, {3,4,5}, {6,7,8}, {0,3,6}, {1,4,7}, {2,5,8}, {0,4,8}, {2,4,6}]

def oneGame():
    shuffled = list(range(9))
    random.shuffle(shuffled)
    for i in range(0, 9, 2):
        placeMarker("x", shuffled[i], i)
        if(checkWinner()):
            break
        if(i < 8):
            placeMarker("o", shuffled[i+1], i+1)
        if(checkWinner()):
            break
    
def placeMarker(m, p, i):
    board[p] = m
    boardOrder[p] = i

def checkWinner():
    ## print(board)
    for i in range(9):
        if(board[i] == "x"):
            x.add(i)
        if(board[i] == "o"):
            o.add(i)
    ## print(x)
    ## print(o)
    for i in winningBoards:
        if(x.issuperset(i)):
            print("Winner x!")
            return True
        if(o.issuperset(i)):
            print("Winner o!")
            return True
    return False

def printBoard(title, board):
    finalBoard = [" " if i is None else i for i in board]
    print(title)
    print("-------")
    print("|" + str(finalBoard[0]) + "|" + str(finalBoard[1]) + "|" + str(finalBoard[2]) + "|")
    print("|" + str(finalBoard[3]) + "|" + str(finalBoard[4]) + "|" + str(finalBoard[5]) + "|")
    print("|" + str(finalBoard[6]) + "|" + str(finalBoard[7]) + "|" + str(finalBoard[8]) + "|")
    print("-------\n")

for i in range(3):
    oneGame()
    printBoard("End Board", board)
    printBoard("Order", boardOrder)

