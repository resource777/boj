n,m,k = map(int,input().split())
f = [list(map(int,input().split())) for _ in range(n)]
ans = -1000000
tmp = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(i,j):
    global ans
    if len(tmp)==k:
        val = 0
        for ii,jj in tmp:
            val+=f[ii][jj]
        ans = max(ans,val)
        return
    
    for ii in range(i,n):
        for jj in range(j if i == ii else 0,m):
            if (ii,jj) in tmp:
                continue
            chk = False
            for kk in range(4):
                nx,ny = ii+dx[kk],jj+dy[kk]
                if (nx,ny) in tmp: 
                    chk = True
                    break
            if not chk:
                tmp.append((ii,jj))
                dfs(ii,jj)
                tmp.pop()
dfs(0,0)
print(ans)