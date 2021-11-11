from oopEx import Calculator

class ChildImp(Calculator):
	numChild = 200

	def __init__(self):
		Calculator.__init__(self,2,5)

	def getCompleteData(self):
		return self.numChild + self.num + self.sumNumbers()

objC = ChildImp()
result = objC.getCompleteData()
print(result)



