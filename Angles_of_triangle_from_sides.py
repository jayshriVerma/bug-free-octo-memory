import math
def angle_solver(sides):
    a, b, c = sides[0], sides[1], sides[2] 
    if (sum(sides)-max(sides))<=max(sides) or any(list(map(lambda x:x<0 or x==0,sides))):
        return "No possible triangle"
    A = math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
    B = math.degrees(math.acos((c**2+a**2-b**2)/(2*c*a)))
    C = math.degrees(math.acos((a**2+b**2-c**2)/(2*a*b)))
    
    A_minute = (math.modf(A)[0]*60)
    B_minute = (math.modf(B)[0]*60)
    C_minute = (math.modf(C)[0]*60)

    A_second= float(round(math.modf(A_minute)[0]*60,2))
    B_second= float(round(math.modf(B_minute)[0]*60,2))
    C_second= float(round(math.modf(C_minute)[0]*60,2))

    return [f"{int(A)}:{int(A_minute)}:{A_second}", f"{int(B)}:{int(B_minute)}:{B_second}", f"{int(C)}:{int(C_minute)}:{C_second}"]

print("claculation of the angles of a triangle using law of cosines a**2 = b**2+c**2-2*b*c*cosA")
sides=[] 
for i in range(0,3):
    x=int(input("Please enter the side of triangle,3 sides are required enter one by one:  "))
    sides.append(x)
print(angle_solver(sides))	  	
