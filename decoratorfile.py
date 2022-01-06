def logged(function):
	def wrapper(*args,**kwargs):
		value=function(*args,**kwargs)
		with open("logfile.txt",'a+') as f:
			fname =function.__name__
			print(f"{fname} returned value as {value}")
			f.write(f"{fname} returned value as {value}\n")
		return value
	return wrapper
	
@logged			
def add(x,y):
	return x+y
print(add(10,20))
print(add(499,899))
print(add(49,89))
