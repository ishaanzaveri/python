#Classes
class person:
	__name = ""
	__email = ""

	def __init__ (self,name,email):
		self.__name = name 
		self.__email = email

	def set_name(self, name):
		self.__name = name  

	def get_name (self):
		return self.__name

	def set_email(self, email):
		self.__email = email  

	def get_email (self):
		return self.__email

	 

brad = person("Brad pitt", "bp@something.com")
#brad.set_name("Brad traversky")
#brad.set_email("brad@example.com ")
 
#print (brad.get_name())
#print (brad.get_email())
#print (brad.to_String())

class customer (person) :
	__balance = 0 

	def __init__(self, name, email, balance): 
		self.__name = name 
		self.__email = email 
		self.__balance = balance 
		super(customer,self).__init__(name,email )
	def Set_balance (self, balance):
		self.__balance = balance  
	def get_balance (self): 
		return self.__balance
	def to_String(self):
		return "{} has a balance of {} and can be contacted at {}".format(self.__name,self.__balance , self.__email)

john = customer("john", "john@yahoo.com", 5000)
print (john.to_String())