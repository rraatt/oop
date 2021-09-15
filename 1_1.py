import sys
# Import sys module for argv function.

inp = ' '.join(sys.argv[1:])
# Join all arguments passed in the command line into a string divided with a whitespace.
print(eval(inp))
# Print calculated equation via eval function.
