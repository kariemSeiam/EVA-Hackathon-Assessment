def isMatch(s, p):
 
    n = len(s)
    m = len(p)
 
    TB = [[False for x in range(m + 1)] for y in range(n + 1)]
 
    TB[0][0] = True
 
    for j in range(1, m + 1):
        if p[j - 1] == '*':
            TB[0][j] = TB[0][j - 1]
 
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                TB[i][j] = TB[i - 1][j] or TB[i][j - 1]
            elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                TB[i][j] = TB[i - 1][j - 1]
 
    return TB[n][m]

print('s = ')
s = input()
print('p = ')
p = input()
print(isMatch(s, p))
done = input()