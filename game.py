from board import Board
from stack import Stack
import random

board_game = Board()

# for testing purposes the pieces will be character 'a', 'b', 'c', 'd', and 'e'

pieces = ['a', 'b', 'c', 'd', 'e']

def randPiece():
    return random.choice(pieces) 

windDir = {0: "North ^", 1: "East >", 2: "South V", 3: "West <"}


# Game loop
while True:
    # ask user where he wants to place it
    newStack = Stack([randPiece(), randPiece()])
    dir = random.randint(0, 3) # North starting at 0 and clockwise til West with value 3
    print(chr(27) + "[2J") # clears screen
    print('The wind is blowing {}'.format(windDir[dir]))
    board_game.draw()
    print("{} is the stack given".format(newStack))
    continueAsking = True # continue to ask the user for valid coors
    while continueAsking: # loop until given valid coors
        x_coor = int(input("Please enter a valid X coor: "))
        y_coor = int(input("Please enter a valid Y coor: "))
        # if valid, do not continue asking
        continueAsking = not board_game.checkPlace(y_coor, x_coor)
    board_game.place(newStack, x_coor, y_coor)
    board_game.blow(dir)
    board_game.draw()





