def iNum(n) :
    i = 1
    flag = 0
    while i < 1000:
        if i == n:
            i = i + 1
            continue
        if i % n == 0:
            x = [int(a) for a in str(i)]
            b = sum(x)
            if b == n:
                flag = 1
                break
        i = i + 1
    if flag == 0:
        i= -1
    return i

lis =[]
def iNumIn(n):
    i = 0
    while i < n:
        s = int(input())
        lis.append(iNum(s))
        i += 1
        if i == n :
            break

    return lis

n = int(input())
iNumIn(n)