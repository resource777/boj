import sys
from collections import deque
n,m,v=map(int,sys.stdin.readline().split())
g=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    g[a].append(b)
    g[b].append(a)
for i in range(1,n+1):
    g[i].sort()
def dfs(i):
    print(i,end=' ')
    for j in g[i]:
        if not vis[j]:
            vis[j]=True
            dfs(j)
def bfs(i):
    tmp=deque()
    vis[i]=True
    tmp.append(i)
    while len(tmp):
        x=tmp.popleft()
        print(x,end=" ")
        for j in g[x]:
            if not vis[j]:
                vis[j]=True
                tmp.append(j)
vis = [False]*(n+1)
vis[v]=True
dfs(v)
print()
vis = [False]*(n+1)
bfs(v)