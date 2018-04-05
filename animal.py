class Animal(object):
	def __init__(self,name,health):
		self.name=name
		self.health=health

	def walk(self):
		self.health-=1
		return self
	def run(self):
		self.health-=5
		return self

	def display_health(self):
		print"Name: {}".format(self.name)
		print"Health: {}".format(self.health)
		return self

class Dog(Animal):
	def __init__(self,name):
		super(Dog,self).__init__(name, 150)

	def pet(self):
		self.health+=5
		return self

class Dragon(Animal):
	def __init__(self,name):
		super(Dragon,self).__init__(name,170)

	def fly(self):
		self.health-=10
		return self

	def display_health(self):
		print"Name: {}".format(self.name)
		print"Health: {}".format(self.health)
		print"I am a Dragon"
		return self



my_dragon = Dragon("Fofo")
my_dragon.run().walk().fly().display_health()

my_dog=Dog("Pupcake")
my_dog.walk().run().pet().display_health()