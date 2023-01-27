from collections import deque
m,n = map(int,input().split())
f = [list(map(int,input().split())) for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
tmp = deque()
for i in range(n):
    for j in range(m):
        if f[i][j]==1:
            tmp.append((i,j))
while tmp:
    cx,cy = tmp.popleft()
    for i in range(4):
        nx,ny = cx+dx[i],cy+dy[i]
        if 0<=nx<n and 0<=ny<m and f[nx][ny]==0:
            f[nx][ny] = f[cx][cy]+1
            tmp.append((nx,ny))
ans=0
zero = False
for i in range(n):
    for j in range(m):
        if f[i][j]==0:
            zero=True
            break
        else:
            ans = max(ans,f[i][j])
if zero:
    print(-1)
else:
    print(ans-1)
