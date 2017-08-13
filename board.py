from stack import Stack
from enum import Enum

class Direction(Enum):
    """
    Going clockwise starting at North
    """
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


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
        If there are any stacks of two, then move the tops of those pieces to 
        new stacks IFF those new stacks are empty.

        pre: dir must be of class Direction
        """


        # make sure that dir is of type Direction
        assert(type(dir) is Direction)

        for row in len(NUM_ROWS):
            for col in len(NUM_COLS):
                if board[row][col].size() == 2:
                    print("I am supposed to check to see if I can land on neighbor")

    def checkNeighbor(row, col, dir):
        """
        Given coordinates to the stack to check with the direction for it to fall in,
        return a boolean on whether top of stack can land in new stack position 
        legally.
        Illegal if:
            * there already existed a non-empty stack.
            * out of bounds

        pre: row and col-  two ints that are both less than NUM_ROWS and NUM_COLS, 
            aka dimesions of the board

            dir - is a type of class Direction
        post: True if stack can legally fall <dir> of coordinates given
            False otherwise
        """
        # given coordinates must be in bounds of board 
        assert(row < NUM_ROWS)
        assrt(col < NUM_COLS)
        # given direction must be of type class Direction
        assert(type(dir) is Direction)
        
        # Depending on direction, the amount of offset is here for checking that neighbor
        # starting from north and going clockwise
        rowOffset = [-1, 0, 1, 0]
        colOffset = [0, 1, 0, -1]
        
