import turtle

class Polygon:
	def __init__(self,sides,name, size=100, color="red", line_thickness=2):
		self.sides = sides
		self.name = name
		self.size = size
		self.color = color
		self.line_thickness = line_thickness
		self.sum_interior_angles = (self.sides -2)*180
		self.angle = self.sum_interior_angles/self.sides
	
	def draw(self):
		turtle.color(self.color)
		turtle.pensize(self.line_thickness)
		for i in range(self.sides):
			turtle.forward(100)
			turtle.right(180-self.angle)
		turtle.done()


class Hexagon(Polygon):
    def	__init__(self, sides=6,name = "Hexagon"):
    	super.__init__()	
		
rectangle = Polygon(4, "rectangle")
pentagon = Polygon(5, "pentagon")
	
print(rectangle.sides)
#print(pentagon.name)
#print(square.sum_interior_angles)
print(rectangle.angle)

Hexagon = Hexagon()
	
rectangle.draw()
hexagon.draw()
