class MathDojo(object):
	def __init__(self,value):
		self.value=value

	def add(self,*plus):
		for element in plus:
			if (type(element) == int):
				self.value += element
			elif (type(element) == list or tuple):
				for a in element: 
					self.value +=a
		return self

	def subtract(self,*sub):
		for element in sub:
			if (type(element)==int):
				self.value-=element
			elif (type(element)==list or tuple):
				#total=0
		 		for b in element:
			 		#total+=b
					self.value-=b
			return self

	def result(self):
		print"result is {}".format(self.value)
		return self
md=MathDojo(0)
md.add([2,3],5).add([2],1,5).subtract([3,1]).result()