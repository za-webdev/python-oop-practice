class Car(object):
	def __init__(self,price,speed,fuel,milage):
		self.price=price
		self.speed=speed
		self.fuel=fuel
		self.milage=milage

	def display_all(self):
		print "Price:{}".format(self.price)
		print "Speed:{}".format(self.speed)
		print "Fuel:{}".format(self.fuel)
		print "Milage:{}".format(self.milage)
		if self.price>10000:
			print"Tax:0.15"
		else:
			print"Tax:0.12"
		



car_1=Car(2000,"35mph","full","15mpg")
car_2=Car(2000,"5mph"," not full","105mpg")
car_3=Car(2000,"15mph","kind of full","105mpg")
car_4=Car(2000,"25mph","full","25mpg")
car_5=Car(2000,"45mph","full","25mpg")
car_6=Car(20000000,"35mph","empty","15mpg")



