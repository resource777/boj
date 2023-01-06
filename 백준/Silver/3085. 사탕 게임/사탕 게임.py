n = int(input())
f = [[i for i in input()] for _ in range(n)]
ans = 1

def check(f):
    ans = 1
    for i in range(n):
        val = 1
        for j in range(n-1):
            if f[i][j] == f[i][j+1]:
                val+=1
                ans = max(ans,val)
            else:
                val = 1
    for j in range(n):
        val = 1
        for i in range(n-1):
            if f[i][j] == f[i+1][j]:
                val+=1
                ans = max(ans,val)
            else:
                val = 1
    return ans

for i in range(n):
    for j in range(n-1):
        me, you = f[i][j],f[i][j+1]
        f[i][j],f[i][j+1] = f[i][j+1],f[i][j]
        ans = max(check(f),ans)
        f[i][j],f[i][j+1] = me,you
for j in range(n):
    for i in range(n-1):
        me, you = f[i][j],f[i+1][j]
        f[i][j],f[i+1][j] = f[i+1][j],f[i][j]
        ans = max(check(f),ans)
        f[i][j],f[i+1][j] = me,you
print(ans)

