#!/bin/python3

import sys


t = int(input().strip())
l=[]
for a0 in range(t):
    n = int(input().strip())    
    l.append(n)    
def ispal(x):
    return True if str(x) == str(x)[::-1] else False

lst = set(a*b for a in range(999, 99, -1) for b in range(a, 99, -1) if ispal(a*b))


for N in l:
    mx = max(i for i in lst if i < N)
    print(mx)
