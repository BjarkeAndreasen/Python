"""
Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a
 comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
"""

import sys
import math
	
def main():
	words = [x for x in sys.argv[1].split(',')]
	words.sort()
	print(','.join(words))

if __name__ == '__main__':
	main()