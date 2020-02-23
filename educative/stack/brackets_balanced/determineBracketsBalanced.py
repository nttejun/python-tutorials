from brackets_balanced.stack import Stack


def isMatch(parent, child):
    if parent == "{" and child == "}":
        return True
    elif parent == "[" and child == "]":
        return True
    elif parent == "(" and child == ")":
        return True
    else:
        return False


def checkBalance(checkValue):
    stack = Stack()
    isBalanStatus = True
    index = 0

    while index < len(checkValue) and isBalanStatus:
        child = checkValue[index]
        if child in "([{":
           stack.push(child)
        else :
            if stack.is_empty():
                isBalanStatus = False
            else :
                parent = stack.pop()
                if not isMatch(parent, child):
                    isBalanStatus = False

        index += 1

    if stack.is_empty() and isBalanStatus:
        return True
    else:
        return False



balanceSample = ["{", "{", "(", ")", "}", "}"]
sampleResult = checkBalance(balanceSample)
print(sampleResult)

balanceSample = ["{", "{", "(", ")", "}", "}", ")", ")"]
sampleResult = checkBalance(balanceSample)
print(sampleResult)

