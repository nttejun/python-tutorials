class Stack():
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        return self.values.pop()

    def peek(self):
        if not self.is_empty():
            return self.values[-1]

    def is_empty(self):
        return self.values == []

