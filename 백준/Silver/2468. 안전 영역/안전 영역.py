import sys
sys.setrecursionlimit(10**5)
n =  int(input())
f = [list(map(int,input().split())) for _ in range(n)]
v = [[0]*n for _ in range(n)]
answer=1
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(i,j,h):
    v[i][j]=1
    for k in range(4):
        nx,ny = i+dx[k],j+dy[k]
        if 0<=nx<n and 0<=ny<n and v[nx][ny]==0 and f[nx][ny]>h:
            dfs(nx,ny,h)
ans = []
for h in range(100):
    cnt=0
    for i in range(n):
        for j in range(n):
            if v[i][j]==0 and f[i][j]>h:
                dfs(i,j,h)
                cnt+=1
    ans.append(cnt)
    v = [[0]*n for _ in range(n)]
print(max(ans))