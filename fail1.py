# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 11:24:31 2016

@author: weir
"""
'''有问题，height和base永远不可能是float类型，只能是str类型

import math

#get base
inputOK = False
while not inputOK:
    base=input('enter base:')
    if type(base)==type(1.0):inputOk = True
    else:print('error')
       
#get height
inputOK = False
while not inputOK:
    height =input('enter height:')
    if type(height)==type(1.0):
        inputOk = True
    else:
        print('error')
        
hyp = math.sqrt(base*base+height+height)

print('base:',str(base),',height:',str(height),',hyp:',str(hyp))
