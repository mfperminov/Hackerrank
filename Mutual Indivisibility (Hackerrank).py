import sys
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        a, b, x = input().strip().split(' ')
        a, b, x = [int(a), int(b), int(x)]
        ans=[]
        for i in range (b,a-1,-1):
            for j in range (b,a-1,-1):
                if gcd(i,j)==1 and i!=j and i not in ans:
                    ans.append(i)
            if len(ans)==x:
                    break

        if len(ans)>=x:
            ans2=ans
            for item in ans2:
                for item2 in ans2:
                    if gcd(item, item2)!=1 and item!=item2:
                      ans.remove(item)
        if len(ans)>=x:
            print(*ans)
        else:
            print(-1)
