"""
Modified version of a stack class
    Modified:
        * peek_all()
        * only two items may be in this stack at a time

This file solely contains template class for any type of stack
data structure
"""
class Stack:
    """

    [btm of stack, top of stack]

    """


    def __init__(self, con):
        self.size = 0
        self.con = con

    def is_empty(self):
        """
        return whether the con is basically empty
        """
        return self.con == []

    def push(self, item):
        """
        Adds an item to the end of the list.

        Stack cannot be more than 2 units long, for the sake of this board.py and game.py
        """
        if self.get_size() < 2:
            self.con.append(item)
        else:
            raise ValueError

    def pop(self):
        """
        Remove and return the top of the stack (ie end of con)
        """
        return self.con.pop()

    def peek(self):
        """
        Return the value of the top of the stack without removing it
        """
        if self.is_empty():
            return None
        return self.con[self.get_size() - 1]

    def get_size(self):
        """
        return the size of the stack
        """
        return len(self.con)

    def peek_all(self):
        """
        return a copy of the whole list without removing
        anything in this one
        """
        return self.con # [btm, top]

    def __str__(self):
        return str(self.con)
