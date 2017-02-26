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
		print("Usage: TBD")
		sys.exit(1)

	#numbers_tuple = {}
	#for arg in args:
	#	tuple[args]

	text = ""
	tuple_text = tuple(args)
	for arg in args:
		if text == "":
			text = arg
		else:
			text = text + ',' + arg

	
	print (text)
	print (tuple_text)

if __name__ == '__main__':
	main()