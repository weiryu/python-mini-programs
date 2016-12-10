# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 10:25:42 2016

@author: weir
搜索算法
"""

'''顺序搜索'''
def search(s,e):
    answer = None
    i=0
    numCompares=0
    while i<len(s) and answer==None:
        numCompares+=1
        if e==s[i]:
            answer=True
        elif e<s[i]:
            answer=False
        i+=1
    print(answer,numCompares)
    
'''二分法搜索'''
def bsearch(s,e,first,last):
    print(first,last)
    if (last-first)<2:
        return s[first]==e or s[last]==e
    mid=first+(last-first)/2
    if s[mid]==e:
        return True
    if s[mid]>e:
        return bsearch(s,e,first,mid-1)
    return bsearch(s,e,mid+1,last)
    
def search1(s,e):
    print(bsearch(s,e,0,len(s)-1))
    print('search complete')
    
def testSearch():
    s=range(0,100000)
    input('basic,-1')
    print(search(s,-1))
    input('binary,-1')
    print(search1(s,-1))
    input('basic,end')
    print(search(s,100000))
    input('binary,end')
    print(search1(s,100000))
    s=range(0,1000000)
    input('basic,partway')
    print(search(s,1000000))
    input('binary,larger end')
    print(search1(s,1000000))
    input('binary,partway')
    print(search(s,1000000))
    input('binary,larger end')
    print(search1(s,1000000))
        