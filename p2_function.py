def circle(radius):
    return 3.14*radius*radius
def rectangle(l,b):
    return l*b
def square(s):
    return s*s
def ratriangle(h,b):
    return h*b*0.5
r=int(input(" enter radius of circle => "))
l=int(input(" enter length of rectangle => "))
b=int(input(" enter breadth of rectangle => "))
s=int(input(" enter square side => "))
h=int(input(" enter height of triangle => "))
base=int(input(" enter base of triangle => "))
print("Area of  CIRCLE  => ",circle(r)," sq units")
print("Area of  RECTANGLE => ",rectangle(l,b)," sq units")
print("Area of  SQUARE => ",square(s)," sq units")
print("Area of   RIGHT ANGLE TRIANGLE => ",ratriangle(h,base)," sq units")



