class Product(object):
	def __init__(self,itemname,price,weight,brand):
		self.price=price
		self.itemname=itemname
		self.weight=weight
		self.brand=brand
		self.status="for sale"
		

	def sell(self):
		self.status="sold"

		

	def tax(self):
		self.price= self.price+(self.price*0.15)
		return self

	def return_reason(self,reason):
		if reason=="defective":
			self.status="defective"
			self.price=0
		if reason=="box":
			self.status="for sale"
		if reason=="used":
			self.price=self.price-(self.price*0.2)
		return self

	def displayinfo(self):
		print"\nItem name:{}".format(self.itemname)
		print"Price:{}".format(self.price)
		print"Weight:{}".format(self.weight)
		print"Brand:{}".format(self.brand)
		print"Status:{}".format(self.status)
		return self


handbag=Product("HandBag",300,"0.2lbs","Gucci",)
handbag.displayinfo().return_reason('defective').displayinfo().tax().displayinfo()




