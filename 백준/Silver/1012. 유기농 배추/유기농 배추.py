t = int(input())

for _ in range(t):
    answer = 0
    m,n,k = map(int,input().split())
    f = [[0]*m for _ in range(n)]
    for __ in range(k):
        mm,nn = map(int,input().split())
        f[nn][mm] = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    def dfs(i,j):
        f[i][j] = 0
        for k in range(4):
            nx,ny = i+dx[k],j+dy[k]
            if 0<=nx<n and 0<=ny<m and f[nx][ny]==1:
                dfs(nx,ny)
    for i in range(n):
        for j in range(m):
            if f[i][j] == 1:
                dfs(i,j)
                answer += 1
    print(answer)