 # -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 13:22:45 2020

@author: user
"""
n=int(input("Enter a number: "))
a=[]
while(n>0):
    dig=n%2
    a.append(dig)
    n=n//2
a.reverse()
print("Binary Equivalent is: ")
for i in a:
    print(i,end=" ")
