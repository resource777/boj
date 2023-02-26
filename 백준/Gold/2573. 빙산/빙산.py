from collections import deque
n,m = map(int,input().split())
f = [list(map(int,input().split())) for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
year = 0
y = 1
while True:
    neig = [[0]*m for _ in range(n)]
    v = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(4):
                nx,ny = i+dx[k],j+dy[k]
                if 0<=nx<n and 0<=ny<m and f[nx][ny]==0:
                    neig[i][j]+=1
    zero = 0
    for i in range(n):
        for j in range(m):
            f[i][j]=max(f[i][j]-neig[i][j],0)
            if f[i][j]==0:
                zero+=1
    if zero == n*m:
        break
    dum = 0
    for i in range(n):
        for j in range(m):
            if f[i][j]>0 and v[i][j]==0:
                dum+=1
                q = deque()
                q.append((i,j))
                v[i][j]=1
                while q:
                    cx,cy = q.popleft()
                    for k in range(4):
                        nx,ny = cx+dx[k],cy+dy[k]
                        if 0<=nx<n and 0<=ny<m and v[nx][ny]==0 and f[nx][ny]>0:
                            q.append((nx,ny))
                            v[nx][ny]=1
    if dum>=2:
        year=y
        break
    y+=1
print(year)