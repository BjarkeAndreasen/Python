"""
Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""


import sys
import math
	
def main():
	args = sys.argv[1:]
	if not args:
		sys.exit(1)

	words = sorted(args)
	words_no_duplicates = []
	prev = ""
	for word in words:
		if not word == prev:
			words_no_duplicates.append(word)
		prev = word

	print(words_no_duplicates)

if __name__ == '__main__':
	main()
