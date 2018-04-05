class Call(object):
	def __init__(self,my_id,name,phone,time,reason):
		self.my_id=my_id
		self.name=name
		self.phone=phone
		self.time=time
		self.reason=reason

	def displayall(self):
		print "Id is {}".format(self.my_id)
		print "Name is{}".format(self.name)
		print "Phone number is{}".format(self.phone)
		print "Time of call is{}".format(self.time)
		print "Reason of call is{}".format(self.reason)
		return self
		
class CallCenter(object):
	def __init__(self):
		self.listof_call=[]
		self.lengthofcall_list=0

	def add(self,call):
		self.listof_call.append(call)
		self.lengthofcall_list=len(self.listof_call)
		return self

	def remove(self,call):
		self.listof_call.pop(0)
		self.lengthofcall_list=len(self.listof_call)

		return self

	def info(self):
		print [[x.name,x.phone]for x in self.listof_call]

		# print"Caller name:{}".format(self.name)
		# print"Phone number:{}".format(self.phone)
		print"Length of queue{}".format(self.lengthofcall_list)

caller1=Call(001,"Jeff",555,2,"complaint")
caller2=Call(002,"hell",777,3,"happy")
call_tower=CallCenter()
call_tower.add(caller1).add(caller2).remove(caller2).info()


