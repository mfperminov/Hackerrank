#!/bin/python3

import sys

def saveThePrisoner(n, m, s):
    # Complete this function
    if (m+s-1)<=n:
        return (m+s-1)
    else:
        k=(m-(n-s+1))
        if (k%n)==0:
            return n
        else:
            return (k%n)
t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)
