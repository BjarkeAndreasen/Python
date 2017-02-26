"""
Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
"""

import sys
import math
	
def main():
	numbers = (sys.argv[1].split(','))
	X = int(numbers[0])
	Y = int(numbers[1])

	matrix = [[0 for y in range(Y)] for x in range(X)]
	for numberX in range(0,X):
		for numberY in range(0,Y):
			matrix[numberX][numberY] = numberX*numberY
	print (matrix)

if __name__ == '__main__':
	main()