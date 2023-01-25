import sys
n,m = map(int,sys.stdin.readline().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    g[a].append(b)
    g[b].append(a)
vis = [False]*(n+1)
ans=0
def dfs(v):
    for i in g[v]:
        if not vis[i]:
            vis[i] = True
            dfs(i)
for i in range(1,n+1):
    if not vis[i]:
        vis[i]=True
        dfs(i)
        ans+=1
print(ans)
