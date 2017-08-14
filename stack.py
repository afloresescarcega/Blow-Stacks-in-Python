

class Stack:
    """

    [btm of stack, top of stack]

    """

    def __init__():
        self._size = 0
        self.con = []

    def isEmpty(self):
        return self.con == []

    def push(self, item):
        if(size() < 2):
            self.con.append(item)
        else:
            raise(ValueError)

    def pop(self):
        return self.con.pop()

    def peek(self):
        return self.con[size() - 1]

    def size(self):
        return len(self.con)
    
    def peekAll(self):
        return self.con # [btm, top]



    
