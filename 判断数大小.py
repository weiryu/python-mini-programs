# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 10:04:15 2016

@author: weir
"""


"""方法1"""
"""
from random import randint
x=randint(0,300)
Aflag=True
while Aflag:
    digit=int(input("please:"))
    if digit==x:
        print("bingo")
        Aflag=False
    elif digit>x:
        print("digit is bigger")
    else:
        print("x is bigger")
"""


"""方法2"""
from random import randint
maxtime=int(input("how many times would you like to play:"))
x=randint(0,300)
go='y'
count=0

while (go=='y'):
    digit=int(input("please input digit:"))
    if digit==x:
        print("bingo")
        break
    elif digit>x:
        print("digit is bigger")
    else:
        print("x is bigger")
    count+=1
    if count>=maxtime:
        break
    else:
        print("print 'y' to continue or others to quit:")
        go=input()

print("goodbye")
    
    