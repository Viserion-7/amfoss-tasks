#!/bin/python3

import sys

l=[]
t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    l.append(n)
    

def fib(b):
    ans = 0
    x = 1
    y = 2
    while x < b:
        if x % 2 == 0:
            ans += x
        x, y = y, x + y
    return ans

    
for i in range(t):
    b=l[i]
    c=fib(b)
    print(c)
