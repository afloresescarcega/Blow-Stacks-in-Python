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
# strictly for testing finding matches
TESTING_PIECES = ['a']

def rand_piece():
    """
    returns one of the five random pieces
    in PIECES
    """
    return random.choice(TESTING_PIECES)

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
        row_coor = int(input("Please enter a valid row coor: ")) # pylint: disable=invalid-name
        col_coor = int(input("Please enter a valid col coor: ")) # pylint: disable=invalid-name
        # if valid, do not continue asking
        continue_asking = not BOARD_GAME.check_place(col_coor, row_coor) # pylint: disable=invalid-name
    BOARD_GAME.place(new_stack, row_coor, col_coor)
    BOARD_GAME.blow(dirxn)
    BOARD_GAME.draw()
    BOARD_GAME.find_and_remove_matches()
