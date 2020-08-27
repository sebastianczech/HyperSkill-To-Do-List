class Stack():

    def __init__(self):
        self.list = []

    def push(self, el):
        self.list.append(el)

    def pop(self):
        return self.list.pop(len(self.list) - 1)

    def peek(self):
        return self.list[len(self.list) - 1]

    def is_empty(self):
        return len(self.list) == 0
