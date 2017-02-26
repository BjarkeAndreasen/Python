import sys

class InputOutString(object):
	def __init__(self):
		self.s = ""

	def getString(self, input):
		self.s = input

	def printString(self):
		print (self.s.upper())

def main():
	args = sys.argv[1:]
	if not args:
		print("Usage: TBD")
		sys.exit(1)

	strObj = InputOutString()
	strObj.getString(args[0])
	strObj.printString()


if __name__ == '__main__':
	main()