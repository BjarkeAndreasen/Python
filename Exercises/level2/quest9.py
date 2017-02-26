"""
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
"""


import sys
import math
	
def main():
	args = sys.argv[1:]
	if not args:
		sys.exit(1)

	for arg in args:
		print(arg.upper())

if __name__ == '__main__':
	main()