

class Stack:
    """

    [btm of stack, top of stack]

    """

    def __init__(self):
        self.size = 0
        self.con = []

    def __init__(self, con):
        self.size = 0
        self.con = con

    def isEmpty(self):
        return self.con == []

    def push(self, item):
        if(self.get_size() < 2):
            self.con.append(item)
        else:
            raise(ValueError)

    def pop(self):
        return self.con.pop()

    def peek(self):
        return self.con[self.size() - 1]

    def get_size(self):
        return len(self.con)
    
    def peekAll(self):
        return self.con # [btm, top]

    def __str__(self):
        return str(self.con)



    
