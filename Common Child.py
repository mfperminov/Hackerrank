import sys

def commonChild(s1, s2):
    # Complete this function
    l=[]
    pos=0
    for i in range(len(s1)):
        if s1[i] in s2 and s1[i] not in l and pos<s2.index(s1[i]):
            l.append(s1[i])
            pos=s2.index(s1[i])
    r=[]
    pos=0
    for i in range(len(s2)):
        if s2[i] in s1 and s2[i] not in r and pos<s1.index(s2[i]):
            r.append(s2[i])
            pos=s1.index(s2[i])
    return max(len(l),len(r))
s1 = input().strip()
s2 = input().strip()
result = commonChild(s1, s2)
print(result)
