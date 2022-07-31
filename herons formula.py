#HERONS FORMULA

import math as root

a=float(input("Enter side length a : "))
b=float(input("Enter side length b : "))
c=float(input("Enter side length c : "))

s=(a+b+c)/2

area=root.sqrt(s*(s-a)*(s-b)*(s-c))

print("Area of the triangle is : ",area)





