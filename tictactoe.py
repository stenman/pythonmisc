import random

## NOTE: Got weird results in IDLE because I couldn't figure out "one-line-printing" there. Run in shell...

board = [None] * 9
boardOrder = [None] * 9
x = set()
o = set()
winningBoards = [{0,1,2}, {3,4,5}, {6,7,8}, {0,3,6}, {1,4,7}, {2,5,8}, {0,4,8}, {2,4,6}]
xwins = 0
owins = 0
nowins = 0

def oneGame():
    resetGame()
    shuffled = list(range(9))
    random.shuffle(shuffled)
    for i in range(0, 9, 2):
        placeMarker("x", shuffled[i], i)
        if(checkWinner()):
            return 0
        if(i < 8):
            placeMarker("o", shuffled[i+1], i+1)
        if(checkWinner()):
            return 1
    return 2
    
def placeMarker(m, p, i):
    global board, boardOrder
    board[p] = m
    boardOrder[p] = i

def checkWinner():
    global x, o, board
    for i in range(9):
        if(board[i] == "x"):
            x.add(i)
        if(board[i] == "o"):
            o.add(i)
    for i in winningBoards:
        if(x.issuperset(i)):
            return True
        if(o.issuperset(i)):
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

def resetGame():
    global board, boardOrder, x, o
    board = [None] * 9
    boardOrder = [None] * 9
    x = set()
    o = set()
    
for i in range(100000):
    result = oneGame()
    if(result == 0):
        xwins = xwins + 1
    if(result == 1):
        owins = owins + 1
    if(result == 2):
        nowins = nowins + 1
    xproc = (xwins / (xwins + owins + nowins)) * 100
    oproc = (owins / (xwins + owins + nowins)) * 100
    noproc = (nowins / (xwins + owins + nowins)) * 100
    print('\rx wins: [%d%%]'%xproc, end="")
##    printBoard("End Board", board)
##    printBoard("Order", boardOrder)

print("\n")
print("x wins total: " + str(xwins) + " (" + str(round(xproc, 1)) + "%)")
print("o wins total: " + str(owins) + " (" + str(round(oproc, 1)) + "%)")
print("no one wins total: " + str(nowins) + " (" + str(round(noproc, 1)) + "%)")

