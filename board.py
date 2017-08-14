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
        # starting from north and going clockwise
        rowOffset = [-1, 0, 1, 0]
        colOffset = [0, 1, 0, -1]



        # make sure that dir is of type Direction
        assert(type(dir) is Direction)

        for row in len(NUM_ROWS):
            for col in len(NUM_COLS):
                if self.board[row][col].size() == 2:
                    # Check to see if I can land on this neighbor, if true, then can land
                    if checkNeighbor(row, col, dir):
                        # Pop off from current stack and move it over
                        piece = self.board[row] [col].pop()
                        # place it in the neighboring cell according to direction
                        self.board[row + rowOffset[dir]] [col + colOffset[dir]].push(piece)

    def checkPlace(row, col):
        """ 
        Given coordinates to the stack to check to see if a full stack can be placed down.
        i.e. is the spot empty?

        return false if
            * there already extied a non-empty stack
            * out of bounds

        return true otherwise
        """
        # given coordinates must be in bounds of board 
        assert(row < NUM_ROWS)
        assert(col < NUM_COLS)

        # check to see that 'row, and col' place is not out of bounds
        # first check row 
        if row < 0 or row >= NUM_ROWS:
            return False
        # next check col
        if col < 0 or col >= NUM_COLS:
            return False

        # check to see if there already exists a stack
        if not self.board[row] [col].isEmpty():
            return False # Has an item , may not place another on this stack
        return True # There seems to be nothing illegal about the placement

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
        # given direction must be of type class Direction
        assert(type(dir) is Direction)
        
        # Depending on direction, the amount of offset is here for checking that neighbor
        # starting from north and going clockwise
        rowOffset = [-1, 0, 1, 0]
        colOffset = [0, 1, 0, -1]

        return checkPlace(row + rowOffset[dir], col + colOffset[dir])

    def draw(self):
        """ 
        Visualizes the board by printing the contents of the cells


        +---+
        |B T| <-- That is a cell;    T represents the item on top B represents the item on the bottom
        +---+
        """
        topAndBtm = "+---+"
        item = "|{} {}|"

        def drawAllBorder():
            for c in range(NUM_COLS):
                print(topAndBtm + '\n') # whole border and moves to new line

        def stringBuilder(*arg):
            return ''.join(arg)

        bufferText = ""

        for i in range(NUM_ROWS):
            drawAllBorder()
            for j in range(NUM_COLS):
                if self.board[i] [j].isEmpty(): # if empty print an empty cell
                    bufferText = stringBuilder(bufferText, item.format(' ', ' '))
                else: # not empty; must peek at all the items and grab individual items
                    contentsOfStack = self.board[i] [j].peekAll()
                    if contentsOfStack[1] is None: # only bottom item of stack because only two items can be in this stack
                        bufferText = stringBuilder(bufferText, item.format(contentsOfStack[0], ' '))
                    else: # stack is full, so print both of the contents
                        bufferText = stringBuilder(bufferText, item.format(contentsOfStack[0], contentsOfStack[1]))
            # print a new line for the bottom border of this row
            print('\n')
            drawAllBorder() # end this row of cells
