# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

'''a的b次方'''

'''
2+3b->时间复杂度O(b)
def exp1(a,b):
    ans=1
    while(b>0):
        ans*=a
        b-=1
    return ans
'''

'''
t(b)=t(b-1)+3->时间复杂度O(b)
def exp2(a,b):
    if b==1:
        return a
    else:
        return a*exp2(a,b-1)
'''

'''
a^b=(a*a)^(b/2)(b:even)=a*(a^(b-1))(b:odd)
b:even->t(b)=6+t(b/2)
b:odd->t(b)=6+t(b-1)=12+t((b-1)/2)
b->12+t(b/2)=12+t(b/4)
done when b/2^k=1->时间复杂度O(log2b)
def exp3(a,b):
    if b==1:
        return a
    if b%2==0:     #判断b是否为偶数
        return exp3(a*a,b/2)
    else:
        return a*exp3(a,b-1)
'''

'''m的n次方'''
'''时间复杂度O(n^2)
def g(n,m):
    x=0
    for i in range(n):
        for j in range(m):
            x+=1
    return x
'''

'''汉诺塔问题'''
'''
t(n)=1+t(1)+2t(n-1)=3+2t(n-1)=3+2*3+4t(n-2)=3(1+2+4+~+2^(k-1)+2^kt(n-k)
时间副复杂度O(2^n)
def tower(size,fromStack,toStack,spareStack):
    if size==1:
        print('move disk from ',fromStack,'to ',toStack)
    else:
        tower(size-1,fromStack,spareStack,toStack)
        tower(1,fromStack,toStack,spareStack)
        tower(size-1,spareStack,toStack,fromStack)