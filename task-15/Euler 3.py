#!/bin/python3

import sys

l=[]
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    l.append(n)
  
import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True

def maxPrimeFactor(n):
    max = 1
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            if isPrime(n//i) and n//i > max:
                max = n//i
                break
            elif isPrime(i): max = i        
    return max
for k in l:
    print(maxPrimeFactor(k))
