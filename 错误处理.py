# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 10:22:12 2016

@author: weir
"""

try:
    num1=int(input("the first number:"))
    num2=int(input("the second number:"))
    print(num1/num2)
except(ValueError,ZeroDivisionError):
    print("invalid input")
else:
    print("haha")
