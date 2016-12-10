# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 17:09:12 2016

@author: weir
二分法求解方程
"""


def squareRoot(x,epsilon):
    assert epsilon>0,'epsilon must be positive,not'+str(epsilon)
    low=0
    high=max(x,1)
    guess=(low+high)/2.0
    ctr=1
    while abs(guess**2-x)>epsilon and ctr<=100:
        if guess **2<x:
            low=guess
        else:
            high=guess
        guess=(low+high)/2.0
        ctr+=1
    assert ctr<=100,'iteration count exceed'
    print('num iteraction:',ctr,'estimate:',guess)
    return guess