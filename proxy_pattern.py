from abc import ABCMeta, abstractstaticmethod

class IBook(metaclass=ABCMeta):

	@abstractstaticmethod
	def student_book():
		"""Interface method"""

class BasicBook(IBook):

	def student_book(self):
		print("The books are really good")

class AdvanceBook(IBook):
	
	def __init__(self):
		self.book=BasicBook()	


	def student_book(self):
		print("The books are very descriptive")
		self.book.student_book()


b1=BasicBook()
b1.student_book()

b2=	AdvanceBook()
b2.student_book()