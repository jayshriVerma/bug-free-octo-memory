from abc import ABCMeta, abstractstaticmethod

class Person(metaclass=ABCMeta):

	@abstractstaticmethod
	def print_data():
		pass

class PersonSingleton(Person):

	__instance=None#private 

	@staticmethod
	def get_static():
		if PersonSingleton.__instance==None:
			#print("Error")
			PersonSingleton("Default Name",0)
		return PersonSingleton.__instance

	def __init__(self,name,age):#intializer or constructor
		if PersonSingleton.__instance!=None:
			raise Exception("Singleton class cannot be instantiated twice!")
		else:	
			self.name=name
			self.age=age
			PersonSingleton.__instance=self

	@staticmethod		
	def print_data():
		print(f"Name:{PersonSingleton.__instance.name},Age:{PersonSingleton.__instance.age}")




p3=PersonSingleton("Sushma",30)
print(p3)
p3.print_data()
p3.get_static()# gives the memory location