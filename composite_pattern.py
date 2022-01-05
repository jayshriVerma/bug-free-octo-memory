from abc import ABCMeta,abstractmethod, abstractstaticmethod

class InterfaceCl(metaclass=ABCMeta):

	@abstractmethod
	def __init__(self,employees):
		"""implement in child class"""

	@abstractstaticmethod
	def print_department(self,employees):
		"""implement in child class"""
		
class ManagerDept(InterfaceCl):

	def __init__(self,employees):
		self.employees=employees
		
		
	def print_department(self):
		print(f'ManagerialDept employees:{self.employees}')

class BankDept(InterfaceCl):

	def __init__(self,employees):
		self.employees=employees
		
		
	def print_department(self):
		print(f'ManagerDept employees:{self.employees}')

class HeadDept(InterfaceCl):

		def __init__(self,employees):
			self.employees=employees
			self.base_employees=employees
			self.s_dept=[]

		def add(self,dept):
			self.s_dept.append(dept)
			self.employees+=dept.employees

		def print_department(self):
			print("HeadDept")
			print(f'Total number of employees:{self.employees}')
			for i in self.s_dept:
				i.print_department()
			print(f'Total number of HeadDept employees:{self.base_employees}')
			

objj1=ManagerDept(200)
objj2=BankDept(130)
parent_dpt=HeadDept(20)	
parent_dpt.add(objj1)
parent_dpt.add(objj2)
parent_dpt.print_department()			






			