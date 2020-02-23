def reverseString(reverseTarget):
    index = 0
    while index < len(reverseTarget):
        reverseTarget = reverseTarget[::-1]
        index += 1

    return reverseTarget


str = "Sample"
print(str[::-1])
print(reverseString(str))
