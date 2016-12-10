# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 09:07:50 2016

@author: weir
程序本身有问题，输入的是str类型永远不可能是真
"""

import math

'''method 1'''
#Get base
inputOK = False
while not inputOK:
    base = input('enter base:')
    if type(base)==type(1.0):
        inputOK=True
    else:
        print('error')

#Get height
inputOK = False
while not inputOK:
    height = input('enter height:')
    if type(height)==type(1.0):
        inputOK=True
    else:
        print('error')

hyp=math.sqrt(base*base+height*height)

print('base:'+str(base)+',height:'+str(height)+',hyp:'+str(hyp))

'''method 2 '''

def getFloat(requestMsg,errorMsg):
    inputOK = False
    while not inputOK:
        val=input(requestMsg)
        if type(val)==type(1.0):
            inputOk=True
        else:
            print('errorMsg')
    return val
    
base=getFloat('enter base:','error:base must be a float')
height=getFloat('enter height:','error:height must be a float')
hyp=math.sqrt(base*base+height*height)

print('base:'+str(base)+',height:'+str(height)+',hyp:'+str(hyp))

    