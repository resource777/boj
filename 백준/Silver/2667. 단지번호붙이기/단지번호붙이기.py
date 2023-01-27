n = int(input())
f = [[int(i) for i in input()] for _ in range(n)]
v = [[0]*n for _ in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def dfs(i,j,num):
    for k in range(4):
        nx = i+dx[k]
        ny = j+dy[k]
        if 0<=nx<n and 0<=ny<n and (v[nx][ny]==0) and (f[nx][ny]==1):
            v[nx][ny] = num
            dfs(nx,ny,num)
number = 1
for i in range(n):
    for j in range(n):
        if (not v[i][j]) and (f[i][j]==1):
            v[i][j]=number
            dfs(i,j,number)
            number+=1
number-=1
print(number)
cnt = [0]*(number+1)
for i in range(n):
    for j in range(n):
        cnt[v[i][j]]+=1
tmp=[]
for i in range(1,number+1):
    tmp.append(cnt[i])
tmp.sort()
print(*tmp,sep="\n")