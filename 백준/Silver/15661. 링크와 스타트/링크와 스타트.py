import sys
n = int(sys.stdin.readline())
f = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
ans = 40000
visit = [False]*n
def dfs(i):
    global ans
    if i==n-1:
        start = 0
        link = 0
        for j in range(n):
            for k in range(n):
                if visit[j] and visit[k]:
                    start+=f[j][k]
                elif not visit[j] and not visit[k]:
                    link+=f[j][k]
        ans = min(ans,abs(start-link))
        return
    for j in range(i+1,n):
        visit[j]=True
        dfs(j)
        visit[j]=False
dfs(-1)
print(ans)