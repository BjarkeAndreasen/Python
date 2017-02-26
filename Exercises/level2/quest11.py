"""
Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

"""

import sys
import math
	
def main():
	args = sys.argv[1:]
	for number in args:
		parts = number.split(',')

	result = []

	for number in parts:	
		numberp = int(number, 2)
		if numberp % 5 == 0:
			result.append(number)

	print(result)

if __name__ == '__main__':
	main()
