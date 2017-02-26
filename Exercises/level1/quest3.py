import sys

def calculate(number):
	result = {}
	for i in range(1, number+1):
		result[i] = i*i

	return result
	
	
	return result

def main():
	args = sys.argv[1:]
	if not args:
		print("Usage: number")
		sys.exit(1)

	number = int(args[0])

	result = calculate(number)
	print(result)


if __name__ == '__main__':
	main()