"""
Contains the game client for BlowStacks the game

please ignore '# pylint: disable=invalid-name' comments throughout my code
It's for my own personal sanity
"""
import random

from board import Board
from stack import Stack

BOARD_GAME = Board()

# for testing purposes the pieces will be character 'a', 'b', 'c', 'd', and 'e'

PIECES = ['a', 'b', 'c', 'd', 'e']

def rand_piece():
    """
    returns one of the five random pieces
    in PIECES
    """
    return random.choice(PIECES)

WIND_DIR = {0: "North ^", 1: "East >", 2: "South V", 3: "West <"}


# Game loop
while True:
    # ask user where he wants to place it
    new_stack = Stack([rand_piece(), rand_piece()]) # pylint: disable=invalid-name
    # North starting at 0 and clockwise til West with value 3
    dirxn = random.randint(0, 3)  # pylint: disable=invalid-name
    print(chr(27) + "[2J") # clears screen
    print('The wind is blowing {}'.format(WIND_DIR[dirxn]))
    BOARD_GAME.draw()
    print("{} is the stack given".format(new_stack))
    # continue to ask the user for valid coors
    continue_asking = True  # pylint: disable=invalid-name
    while continue_asking: # loop until given valid coors
        x_coor = int(input("Please enter a valid X coor: ")) # pylint: disable=invalid-name
        y_coor = int(input("Please enter a valid Y coor: ")) # pylint: disable=invalid-name
        # if valid, do not continue asking
        continue_asking = not BOARD_GAME.check_place(y_coor, x_coor) # pylint: disable=invalid-name
    BOARD_GAME.place(new_stack, x_coor, y_coor)
    BOARD_GAME.blow(dirxn)
    BOARD_GAME.draw()
