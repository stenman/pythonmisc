import random

## Function:    Simulate TicTacToe games using two really stupid computer players.
##              Yup. That's it!
##
## NOTE:    Got weird "one-line-printing" results in IDLE because I couldn't figure out how it works there.
##          Run in some shell instead.

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

print("\n")
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
    print("\r", end='', flush=True)
    print('Games played: {0}       x wins: [{1:.1f}%]        o wins: [{2:.1f}%]        no one wins: [{3:.1f}%]'.format(i+1, xproc, oproc, noproc), end='', flush=True)
##    printBoard("End Board", board)
##    printBoard("Order", boardOrder)

print("\n")
print("Total games: \t\t" + str(xwins + owins + nowins))
print("x wins total: \t\t" + str(xwins) + " (" + str(round(xproc, 1)) + "%)")
print("o wins total: \t\t" + str(owins) + " (" + str(round(oproc, 1)) + "%)")
print("no one wins total: \t" + str(nowins) + " (" + str(round(noproc, 1)) + "%)")

