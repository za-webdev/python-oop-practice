class Bike(object):
	def __init__(self,price, max_speed):
		self.price=price
		self.max_speed=max_speed
		self.miles=0
 
	def ride(self):
		print"ride"
		self.miles+=10
		return self

	def reverse(self):
		if self.miles>=5:
			self.miles-=5
			print"reverse"
		elif self.miles<=0:
			print "Can't reverse"
		return self

	def displayInfo(self):
		print'Bikes price {}, max speed is {} and total miles are {}'.format(self.price,self.max_speed,self.miles)
		return self


bike_1=Bike(200,'25mph')
bike_2=Bike(400,'35mph')
bike_3=Bike(500,'20mph')

#print bike_1.ride().reverse().reverse().reverse().displayInfo()

#print bike_2.ride().ride().reverse().reverse().displayInfo()

print bike_3.reverse().reverse().reverse().displayInfo()



