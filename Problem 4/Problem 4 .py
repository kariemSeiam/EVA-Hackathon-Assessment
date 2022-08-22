import math
lis=[]
def lcm(n):
    Sum = 0
    for i in range(1, n + 1):
        lcm = abs(i * n) // math.gcd(i, n)
        Sum = Sum + lcm
    return Sum

def lcmIn(n):
    i = 0
    while i < n :
        s = int(input())
        lis.append(lcm(s))
        i += 1
        if i == n :
            break

    return lis

n = int(input())
lcmIn(n)