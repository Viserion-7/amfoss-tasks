#!/bin/python3

import sys

l=[]
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    l.append(n)

f = lambda a: a * (a + 1) // 2

def solution(n):
    n -= 1
    return 3 * f(n//3) + 5 * f(n//5) - 15 * f(n//15)


for a in l:
    print(solution(a)) 
