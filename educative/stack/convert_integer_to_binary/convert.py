from stack import Stack


def convert_integer_to_binary(value):
    stack = Stack()

    while value > 0:
        reminder = value % 2
        stack.push(reminder)
        value = value // 2

    binary_number = ""
    while not stack.is_empty():
        binary_number += str(stack.pop())

    return binary_number

print(convert_integer_to_binary(242))

