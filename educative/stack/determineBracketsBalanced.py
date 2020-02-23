from stack import Stack


def isBalanced(balanceCheckString):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(balanceCheckString) and is_balanced:
        open = balanceCheckString[index]
        if open in "([{":
            s.push(open)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, open):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


balanceSample = ["{", "{", "(", ")", "}", "}"]
sampleResult = isBalanced(balanceSample)
print(sampleResult)

balanceSample = ["{", "{", "(", ")", "}", "}", "}"]
sampleResult = isBalanced(balanceSample)
print(sampleResult)