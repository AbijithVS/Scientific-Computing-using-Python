# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:43:07 2020

@author: user
"""

num=int(input("Enter Marks:"))

if num>100:
    print("out of range")
elif num>=90 and num<=100:
    print("GRADE=S")
elif num>=80 and num<90:
    print("GRADE=A")
elif num>=70 and num<80:
    print("GRADE=B")
elif num>=60 and num<70:
    print("GRADE=C")
elif num>=50 and num<60:
    print("GRADE=D")
elif num>=40 and num<50:
    print("GRADE=E")
else:
    print("GRADE=F")

   