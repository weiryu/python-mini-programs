# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
def squareRootNR(x,epsilon):
    assert x>=0,'x must be non-negative,not'+str(x)
    assert epsilon>0,'epsilon must be positive,not'+str(epsilon)
    x= float(x)
    guess = x/2.0    
    diff=guess**2-x
    ctr=1
    while abs(diff)>epsilon and ctr<100:
        guess = guess-diff/(2.0*guess)
        diff =guess**2-x
        ctr+=1
    assert ctr<=100
    print("NR method:",ctr,'estimate:',guess)
    return guess