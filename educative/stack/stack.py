class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

myStack = Stack()
print(myStack.is_empty())
myStack.push("HELLo")
myStack.push("WORLD")
myStack.push("!!!!")
print(myStack.get_stack())
myStack.pop()
print(myStack.get_stack())
print(myStack.is_empty())
print(myStack.peek())
