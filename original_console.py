def add(a,b):
    print(a+b)
def subtract(a,b):
    print(a-b)
def multiply(a,b):
    print(a*b)
def divide(a,b):
    if b!=0:
        print(a/b)
    else:
        print("Cannot divide by zero")
def floor(a,b):
    if b!=0:
        print(a//b)
    else:
        print("Cannot divide by zero")
def power(a,b):
    print(a**b)
def area_square(s):
    print(s*s)
def parameter_square(s):
    print(4*s)
def area_rectangle(a,b):
    print(a*b)
def parameter_rectangle(a,b):
    print(2*(a+b))
def area_circle(r):
    print(3.14*(r**2))
def circumference(r):
    print(2*3.14*r)
def area_triangle(a,b):
    print(1/2*(a*b))
def parameter_triangle(a,b,c):
    print(a+b+c)
def area_cone(r,l):
    if r>0 and l>=r:
        print((3.14*r*r)+(3.14*r*l))
    else:
        print("Invalid radius or slant height")
def area_cube(s):
    print(6*s*s)
def area_cuboid(a,b,c):
    print(2*((a*b)+(b*c)+(a*c)))
while True:
    print("1 for calling add")
    print("2 for calling subtract")
    print("3 for calling multiply")
    print("4 for calling divide")
    print("5 for calling floor")
    print("6 for calling power")
    print("7 for area of square")
    print("8 for perimeter of square")
    print("9 for area of rectangle")
    print("10 for perimeter of rectangle")
    print("11 for area of circle")
    print("12 for circumference of circle")
    print("13 for area of triangle")
    print("14 for perimeter of triangle")
    print("15 for total surface area of cone")
    print("16 for surface area of cube")
    print("17 for surface area of cuboid")
    print("18 for exit")
    condition=int(input("enter a condition:"))
    if condition==1:
        i=float(input("enter a number:"))
        j=float(input("enter a number:"))
        add(i,j)
    elif condition==2:
        i=float(input("enter a number:"))
        j=float(input("enter a number:"))
        subtract(i,j)
    elif condition==3:
        i=float(input("enter a number:"))
        j=float(input("enter a number:"))
        multiply(i,j)
    elif condition==4:
        i=float(input("enter a number:"))
        j=float(input("enter a number:"))
        divide(i,j)
    elif condition==5:
        i=float(input("enter a number:"))
        j=float(input("enter a number:"))
        floor(i,j)
    elif condition==6:
        i=float(input("enter a number:"))
        j=float(input("enter a number:"))
        power(i,j)
    elif condition==7:
        i=float(input("enter the side:"))
        area_square(i)
    elif condition==8:
        i=float(input("enter the side:"))
        parameter_square(i)
    elif condition==9:
        i=float(input("enter the length:"))
        j=float(input("enter the breadth:"))
        area_rectangle(i,j)
    elif condition==10:
        i=float(input("enter the length:"))
        j=float(input("enter the breadth:"))
        parameter_rectangle(i,j)
    elif condition==11:
        i=float(input("enter the radius:"))
        if i>=0:
            area_circle(i)
        else:
            print("Radius cannot be negative")
    elif condition==12:
        i=float(input("enter the radius:"))
        if i>=0:
            circumference(i)
        else:
            print("Radius cannot be negative")
    elif condition==13:
        i=float(input("enter the base:"))
        j=float(input("enter the height:"))
        area_triangle(i,j)
    elif condition==14:
        i=float(input("enter the first side:"))
        j=float(input("enter the second side:"))
        k=float(input("enter the third side:"))
        if i+j>k and i+k>j and j+k>i:
            parameter_triangle(i,j,k)
        else:
            print("Invalid triangle sides")
    elif condition==15:
        i=float(input("enter the radius:"))
        j=float(input("enter the slant height:"))
        area_cone(i,j)
    elif condition==16:
        i=float(input("enter the side:"))
        if i>=0:
            area_cube(i)
        else:
            print("Side cannot be negative")
    elif condition==17:
        i=float(input("enter the length:"))
        j=float(input("enter the breadth:"))
        k=float(input("enter the height:"))
        if i>=0 and j>=0 and k>=0:
            area_cuboid(i,j,k)
        else:
            print("Dimensions cannot be negative")
    elif condition==18:
        print("Thank you for using Multi-Purpose Calculator!")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 18")
