
def valid_parentheses(s):

    stack = []
    pairs = {
        ")" : "(",
        "}" : "{",
        "]" : "["
    }

    for char in s:
        if char not in pairs:
            stack.append(char)
        elif not stack or stack.pop() != pairs[c]:
            return False

print(valid_parentheses(s))