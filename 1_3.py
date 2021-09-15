allowed = ['+', '-', '*', '/']
# List of operations, that are allowed in our equation.


def checker(inp):
    if not len(inp):
        return True
    # Checking, if we have passed through the whole string.
    if inp[0].isnumeric():
        return checker(inp[1:])
    # Check if its a number.
    elif inp[0] in allowed:
        if not inp[1].isnumeric():
            return False
        # Two symbols in a row, equation is not correct.
        else:
            return checker(inp[1:])
    else:
        return False
    # Forbidden symbol, equation is not correct


text = input()
if text[0].isnumeric():
    # Check if our first character is a number, as starting with operation is forbidden.
    cond = checker(text)
    print(cond)
    if cond:
        print(eval(text))
else:
    print(False)