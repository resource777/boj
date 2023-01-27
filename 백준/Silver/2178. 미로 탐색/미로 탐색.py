from collections import deque
n,m = map(int,input().split())
f = [[int(i) for i in input()] for _ in range(n)]
tmp = deque([(0,0,1)])
f[0][0]=0
dx = [0,0,-1,1]
dy = [1,-1,0,0]
while tmp:
    cx,cy,block = tmp.popleft()
    for i in range(4):
        nx,ny,nblock = cx+dx[i],cy+dy[i],block+1
        if nx==n-1 and ny==m-1:
            print(nblock)
            tmp=[]
            break
        if 0<=nx<n and 0<=ny<m and f[nx][ny]==1:
            tmp.append((nx,ny,nblock))
            f[nx][ny]=0