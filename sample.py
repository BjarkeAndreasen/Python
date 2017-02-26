import sys

def printThis(text):
	print(text)

def main():
	args = sys.argv[1:]
	if not args:
		print ("Usage: TBD")
		sys.exit(1)

	text = args[0]

	printThis(text)

if __name__ == '__main__':
	main()