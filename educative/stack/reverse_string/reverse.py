from reverse_string.stack import Stack


def reverseString(reverseTarget):
    index = 0
    while index < len(reverseTarget):
        reverseTarget = reverseTarget[::-1]
        index += 1

    return reverseTarget


def stackReverString(stack, reverseTarget):
    for i in range(len(reverseTarget)):
        stack.push(reverseTarget[i])

    reversedValue = ""
    while not stack.is_empty():
        reversedValue += stack.pop()

    return reversedValue

str = "Sample Sameple Sameple"
print(str[::-1])
print(reverseString(str))

stack = Stack()
print(stackReverString(stack, str))


