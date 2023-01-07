n,m = map(int,input().split())
f = [list(map(int,input().split())) for _ in range(n)]
ans = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
v = [[False for _ in range(m)] for __ in range(n)]

def dfs(i,j,num,sum):
    if num == 4:
        return sum+f[i][j]
    val = 0
    for k in range(4):
        nx,ny = i+dx[k],j+dy[k]
        if nx<0 or ny<0 or nx==n or ny==m or v[nx][ny]:
            continue
        v[nx][ny]=True
        x = dfs(nx,ny,num+1,sum+f[i][j])
        val = max(val,x)
        v[nx][ny]=False
    return val
        
for i in range(n):
    for j in range(m):
        v[i][j]=True
        ans = max(dfs(i,j,1,0),ans)
        v[i][j]=False
for i in range(n-1):
    for j in range(m-2):
        ans = max(ans,f[i][j]+f[i][j+1]+f[i][j+2]+f[i+1][j+1])
        ans = max(ans,f[i+1][j]+f[i+1][j+1]+f[i+1][j+2]+f[i][j+1])
for i in range(n-2):
    for j in range(m-1):
        ans = max(ans,f[i][j]+f[i+1][j]+f[i+2][j]+f[i+1][j+1])
        ans = max(ans,f[i][j+1]+f[i+1][j+1]+f[i+2][j+1]+f[i+1][j])
print(ans)