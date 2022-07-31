

p = float(input("Enter the principle amount : "))
r = float(input("Enter the rate of interest : "))
t = float(input("Enter the time in the years: "))

c =  p * (pow((1 + r / 100), t)) 
print("Compound Interest : ", c)
