import random

# x/o vartannat, position rnd 1-9 tills siffrorna "är slut"
# efter varje placering: kolla om någon vunnit

board = [None] * 9
x = set()
o = set()
winningBoards = [{0,1,2}, {3,4,5}, {6,7,8}, {0,3,6}, {1,4,7}, {2,5,8}, {0,4,8}, {2,4,6}]

def oneGame():
    shuffled = list(range(9))
    random.shuffle(shuffled)
    for i in range(0, 9, 2):
        print(i)
        placeMarker("x", shuffled[i])
        if(checkWinner()):
            break
        if(i < 8):
            placeMarker("o", shuffled[i+1])
        if(checkWinner()):
            break
    
def placeMarker(m, p):
    board[p] = m

def checkWinner():
    print(board)
    for i in range(9):
        if(board[i] == "x"):
            x.add(i)
        if(board[i] == "o"):
            o.add(i)
    print(x)
    print(o)
    for i in winningBoards:
        if(x.issuperset(i)):
            print("Winner x!")
            return True
        if(o.issuperset(i)):
            print("Winner o!")
            return True
    return False

def printBoard():
    finalBoard = [" " if i is None else i for i in board]
    print("\nEnd Board")
    print("-------")
    print("|" + finalBoard[0] + "|" + finalBoard[1] + "|" + finalBoard[2] + "|")
    print("|" + finalBoard[3] + "|" + finalBoard[4] + "|" + finalBoard[5] + "|")
    print("|" + finalBoard[6] + "|" + finalBoard[7] + "|" + finalBoard[8] + "|")
    print("-------")

oneGame()
printBoard()

