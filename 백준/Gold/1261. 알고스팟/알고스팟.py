from collections import deque

m,n = map(int,input().split())
f = [list(map(int,input())) for _ in range(n)]
v = [[-1]*m for _ in range(n)]
q = deque()
tmp = deque()
tmp.append((0,0))
v[0][0]=0
dx = [0,0,-1,1]
dy = [1,-1,0,0]

while tmp:
    cx,cy = tmp.popleft()
    q.append((cx,cy))
    for i in range(4):
        nx,ny = cx+dx[i],cy+dy[i]
        if 0<=nx<n and 0<=ny<m and f[nx][ny]==0 and v[nx][ny]==-1:
            tmp.append((nx,ny))
            v[nx][ny]=0
if (n-1,m-1) in q:
    print(0)
else:
    while q:
        cx,cy = q.popleft()
        if cx == n-1 and cy == m-1:
            print(v[cx][cy])
            break
        for i in range(4):
            nx,ny = cx+dx[i],cy+dy[i]
            if 0<=nx<n and 0<=ny<m and f[nx][ny]==0 and v[nx][ny]==-1:
                q.appendleft((nx,ny))
                v[nx][ny]=v[cx][cy]
            elif 0<=nx<n and 0<=ny<m and f[nx][ny]==1 and v[nx][ny]==-1:
                q.append((nx,ny))
                v[nx][ny]=v[cx][cy]+1