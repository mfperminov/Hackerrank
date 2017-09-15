#!/bin/python3

import sys

def timeConversion(s):
    # Complete this function
    if s[-2:]=='PM':
        if s[0:2]=='12':
            m=s[0:-2]
        else:
            k=int(s[0:2])+12
            m=str(k)+s[2:-2]
        return m
    else:
            if s[0:2]=='12':
                m='00'+s[2:-2]         
            else:
                m=s[0:-2]            
    return m
s = input().strip()
result = timeConversion(s)
print(result)