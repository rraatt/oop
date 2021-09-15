import argparse


def action_type(string):
    act = {"add": "+", "subtract": "-", "multiply": "*", "divide": "/"}
    # Define a dictionary, which will transform words int arithmetic signs.
    x = act.get(string)
    if not x:
        print("Unsupported action")
        exit(1)
    return x


parser = argparse.ArgumentParser(description='Perform math functions.')
parser.add_argument('action', metavar='action', type=action_type, help='Define math function')
parser.add_argument('values', metavar='N', type=str, nargs=2, help='Get two values to perform arithmetic operations')
args = parser.parse_args()
# Parse two arguments from the command line a string that defines function and a two member list of values.
equation = args.values
equation.insert(1, args.action)
print(eval(' '.join(equation)))
# Join the arguments in order: values sign value and calculate the equation via eval function.
