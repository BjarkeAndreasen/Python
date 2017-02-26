import sys

def calculate():
	result = []
	for i in range(2000,3200):
		if (i % 7 == 0) and (i % 5 != 0):
			result.append(str(i))
	return result

def main():
	numbers = calculate()
	print(numbers)


if __name__ == '__main__':
	main()