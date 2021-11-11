class Calculator:  # super class
	num = 89  # class variables

	# Constructor
	def __init__(self, a, b):
		self.first = a
		self.second = b
		print("Calculator class - object is created")

	def getData(self):
		print("Calculator class - getData() method")

	def sumNumbers(self):
		return self.first + self.second + self.num + Calculator.num
