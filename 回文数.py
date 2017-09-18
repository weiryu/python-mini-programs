# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

'method 1'
a=input()
flag = True
for i in range(len(a)//2):
    if a[i]!=a[len(a)-i-1]:
        flag=False
        break
if flag:
    print("%s is huiwen number "%a)
else:
    print("%s is not huiwen number "%a)


'method 2'
def isPalindrome(s):
    if len(s)==1:
        return True
    else:
        return s[0]==s[-1] and isPalindrome(s[1:-1])
