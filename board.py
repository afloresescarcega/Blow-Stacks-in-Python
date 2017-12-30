"""
This file builds and runs the board
that is used inside of game.py


Creates a 2D grid of empty Stacks from the stack class in stack.py.

This game is similar to 'Windin', the iOS game, made by 'no-pact'.
Place a stack of two items that are randomly generated on a 2D grid in an empty cell.
After the stack has been placed, the wind will blow it over the top piece.
The wind blows in four different directions.
If a stack, or a single item, is in a cell, an item cannot be added to it if it is blown.

TO-DO:
    get straight lines of 3 or more similar tiles removed from the board
        and scored.
    scoring
    two or more stacks generated and asked to be placed before the wind blows them over.
"""

from stack import Stack

from my_queue import Queue


class Board:
    """
    Stores a 2D grid of stacks.
    Each cell is init with an empty stack
    """
    # Board game sizes is in terms of number of stacks
    NUM_ROWS = 5
    NUM_COLS = 5

    # starting from north and going clockwise
    row_offset = [-1, 0, 1, 0]
    col_offset = [0, 1, 0, -1]

    def __init__(self):
        # Create a 2D List of empty stack objects with NUM_ROWS and NUM_COLS dimensions
        self.board = [[Stack([]) for i in range(self.NUM_COLS)] for j in range(self.NUM_ROWS)]

    def place(self, stack, row, col):
        """
        Given a stack, check to see if it's placement is valid in the form of a boolean
        If can be placed, mutate the board and return True

        pre: stack must be of the class Stack

        """
        # check pre conditions
        if not isinstance(stack, Stack): # value stack must be of the class Stack
            raise ValueError

        if self.check_place(row, col):
            self.board[row][col] = stack
            return True
        else:
            return False


    def blow(self, dirxn):
        """
        If there are any stacks of two, then move the tops of those pieces to
        new stacks IFF those new stacks are empty.

        pre: dir must be of class Direction
        """


        for row in range(self.NUM_ROWS):
            for col in range(self.NUM_COLS):
                cell = self.board[row][col]
                if len(cell.con) == 2:
                    # Check to see if I can land on this neighbor, if true, then can land
                    if self.check_neighbor(row, col, dirxn):
                        # Pop off from current stack and move it over
                        piece = self.board[row][col].pop()
                        # place it in the neighboring cell according to direction
                        self.board[row + self.row_offset[dirxn]][col + self.col_offset[dirxn]].push(piece)

    def find_and_remove_matches(self):
        """
        Finds and removes matches of three or more and then returns the 
        scores points = 10 + 5(n - 3) where n is the number removed

        Creates a 2D temp board with each cell containing information
        of type and total sum of adjacent similar pieces

        On first pass, mark with NONE the cells that do not have a 
        single adjacent of its similar type

        A cell can have 1 to 4 adjacents that are of the similar type


        """
        num_removed = 0
        temp_board = [[0 for y in range(self.NUM_COLS)] for x in range(self.NUM_ROWS)]

        # First pass, count the number of similar adjecent pieces around
        for row in range(self.NUM_ROWS):
            for col in range(self.NUM_COLS):
                for _dir in range(4): # starting north then clockwise
                    tgt_row = row + self.row_offset[_dir] # target row with offset
                    tgt_col = col + self.col_offset[_dir] # target col with offset
                    if self.in_bounds(tgt_row, tgt_col): # is this piece legal
                        # See if adjacent piece is equal to current row and col
                        if self.board[tgt_row][tgt_col].peek() is self.board[row][col].peek():
                            if self.board[tgt_row][tgt_col].is_empty(): # doesn't add empty stacks
                                pass 
                            else:
                                temp_board[row][col] += 1 # add 1 to the count of similar pieces to self.board[row][col]
        # print temp_board for testing purposes
        for row in range(self.NUM_ROWS):
            temp_str = ""
            for col in range(self.NUM_COLS):
                temp_str = temp_str + str(temp_board[row][col]) + " "
            print(temp_str + "\n")


    def find_neighbors(self, tgt_row, tgt_col):
        """
        Returns a list of coordinates of the neighboring
        cells that match the item target
        """
        neighbors = []
        tgt_item = self.board[tgt_row][tgt_col].peek()
        for direc in range(4):
            offset_row_coor = tgt_row + self.row_offset[direc]
            offset_col_coor = tgt_col + self.col_offset[direc]
            item = self.board[offset_row_coor][offset_col_coor].peek()
            if item == tgt_item: # see if neighbor, item, is same as tgt_item
                neighbors.append([offset_row_coor, offset_col_coor])
        return neighbors




    def in_bounds(self, row, col):
        """
        check to see that 'row, and col' place is not out of bounds
        """
        # first check row
        if row < 0 or row >= self.NUM_ROWS:
            return False
        # next check col
        if col < 0 or col >= self.NUM_COLS:
            return False
        return True # Is in bounds 

    def check_place(self, row, col):
        """
        Given coordinates to the stack to check to see if a full stack can be placed down.
        i.e. is the spot empty?

        return false if
            * there already extied a non-empty stack
            * out of bounds

        return true otherwise
        """

        # check to see that 'row, and col' place is not out of bounds
        if not self.in_bounds(row, col):
            return False

        # check to see if there already exists a stack
        if not self.board[row][col].is_empty():
            return False # Has an item , may not place another on this stack
        return True # There seems to be nothing illegal about the placement

    def check_neighbor(self, row, col, dirxn):
        """
        Given coordinates to the stack to check with the dirxnection for it to fall in,
        return a boolean on whether top of stack can land in new stack position
        legally.
        Illegal if:
            * there already existed a non-empty stack.
            * out of bounds

        pre: row and col-  two ints that are both less than NUM_ROWS and NUM_COLS,
            aka dimesions of the board

        post: True if stack can legally fall <dirxn> of coordinates given
            False otherwise
        """

        return self.check_place(row + self.row_offset[dirxn], col + self.col_offset[dirxn])

    def draw(self):
        """
        Visualizes the board by printing the contents of the cells


        +---+
        |B T| <-- That is a cell;    T represents the item on top
        +---+                        B represents the item on the bottom
        """
        border = "+---+"
        item = "|{} {}|"

        def draw_all_border():
            """
            prints '+---+' times the number of cols
                specified in NUM_COLS
            """
            line = "" # buffer string
            for _ in range(self.NUM_COLS):
                line = string_builder(line, border) # whole border and moves to new line
            print(line)


        def string_builder(*arg):
            """
            faster string concat
            arguments: any number of strings to concat
            return one string with all others joined
            """
            return ''.join(arg)


        for i in range(self.NUM_ROWS):
            buffer_text = ""
            draw_all_border()
            for j in range(self.NUM_COLS):
                if self.board[i][j].is_empty(): # if empty print an empty cell
                    buffer_text = string_builder(buffer_text, item.format(' ', ' '))
                else: # not empty; must peek at all the items and grab individual items
                    con_of_stack = self.board[i][j].peek_all()
                    # only bottom item of stack because only two items can be in this stack
                    if self.board[i][j].get_size() == 1:
                        # string of cell with only btm item of stack
                        single_item = item.format(con_of_stack[0], ' ')
                        buffer_text = string_builder(buffer_text, single_item)
                    else: # stack is full, so print both of the contents
                        # string of cell with both items in stack
                        both_items = item.format(con_of_stack[0], con_of_stack[1])
                        buffer_text = string_builder(buffer_text, both_items)
            # print the buffer text
            print(buffer_text)
            draw_all_border() # end this row of cells
