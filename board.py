from stack import Stack
from enum import Enum

class Direction(Enum):
    """
    Going clockwise starting at North

    Yes, I did index starting at one. Deal with it.
    """
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


class Board:
    """
    Stores a 2D grid of stacks.
    Each cell is init with an empty stack
    """
    # Board game sizes is in terms of number of stacks 
    NUM_ROWS = 5
    NUM_COLS = 5 
    
    def __init__():
        # Create a 2D List of empty stack objects with NUM_ROWS and NUM_COLS dimensions
        self.board = [[Stack() for i in range(NUM_COLS)] for j in range(NUM_ROWS)]


    def blow(dir):
        """

        """

