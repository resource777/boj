from collections import deque
m,n,h = map(int,input().split())

f = [[[0]*m for _ in range(n)] for __ in range(h)]
v = [[[-1]*m for _ in range(n)] for __ in range(h)]
dx = [0,0,1,-1,0,0]
dy = [0,0,0,0,1,-1]
dz = [1,-1,0,0,0,0]
for k in range(h):
    for i in range(n):
        f[k][i] = list(map(int,input().split()))
q = deque()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if f[k][i][j]==1:
                q.append((i,j,k,0))
                v[k][i][j]=0
            if f[k][i][j]==-1:
                v[k][i][j]=0
while q:
    cx,cy,cz,days = q.popleft()
    for i in range(6):
        nx,ny,nz = cx+dx[i],cy+dy[i],cz+dz[i]
        if 0<=nx<n and 0<=ny<m and 0<=nz<h and f[nz][nx][ny]==0 and v[nz][nx][ny]==-1:
            q.append((nx,ny,nz,days+1))
            v[nz][nx][ny]=days+1
            f[nz][nx][ny]=1
val = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if v[k][i][j]==-1:
                print(-1)
                exit(0)
            val = max(val,v[k][i][j])
print(val)