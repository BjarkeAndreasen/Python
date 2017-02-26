import sys
import math
	
def main():
	numbers = (sys.argv[1].split(','))

	value = []
	C = 50
	H = 30
	for number in numbers:
		value.append(str(int(round(math.sqrt(2*C*float(number)/H)))))

	print (value)


if __name__ == '__main__':
	main()