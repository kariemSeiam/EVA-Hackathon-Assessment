class Solution:
    def maxStudents(self, seats):
        m, n = len(seats), len(seats[0])
        validity = []
        
        for i in range(m):
            cur = 0
            for j in range(n):
                cur = (cur << 1) + (seats[i][j] == '.')
            validity.append(cur)
            
        def count_bits(n):
            cnt = 0
            while n:
                cnt += 1
                n = n & (n - 1)
            return cnt
        
        dp = [[-1] * (1 << n) for _ in range(m + 1)]
        dp[0][0] = 0
        for i in range(1, m + 1):
            valid = validity[i - 1]
            for j in range(1 << n):
                # check 1. if x is a subset of y, 2. no adjancent valid states.
                if (j & valid) == j and not (j & (j >> 1)):
                    for k in range(1 << n):
                        # no students in the upper left&right position
                        if not (j & (k >> 1)) and not (j & (k << 1)) and dp[i-1][k] != -1:
                            dp[i][j] = max(dp[i][j], dp[i-1][k] + count_bits(j))
                            
        return max(dp[-1])
#a ='[["#",".","#","#",".","#"],[".","#", "#","#","#","."],["#",".", "#", "#",".","#"]]'
#aSplit = a.split('],[')
#numList = len(aSplit)
#i = 0
#while i < numList :
#    numList -= 1
#    aSplit[numList] = aSplit[numList].replace("[", "") 
#    aSplit[numList] = aSplit[numList].replace("]", "") 
#    aSplit[numList] = aSplit[numList].replace(" ", "")
#    aSplit[numList] = aSplit[numList].replace(",", "")
#    aSplit[numList]
#    print(aSplit)
s = input('seats = [["#",".","#","#",".","#"],[".","#", "#","#","#","."],["#",".", "#", "#",".","#"]]')
s = [["#",".","#","#",".","#"],[".","#", "#","#","#","."],["#",".", "#", "#",".","#"]]
print(Solution().maxStudents(s))
input()