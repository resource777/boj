import sys
sys.setrecursionlimit(20000)
t = int(sys.stdin.readline())
for _ in range(t):
    v,e = map(int,sys.stdin.readline().split())
    g = [[] for _ in range(v+1)]
    vis = [False]*(v+1)
    color = [0]*(v+1)
    flag = False
    for __ in range(e):
        a,b = map(int,sys.stdin.readline().split())
        g[a].append(b)
        g[b].append(a)
    def dfs(i,c):
        global flag
        if flag:
            return
        for j in g[i]:
            if vis[j] and color[j]==color[i]:
                flag=True
                return
            if not vis[j]:
                vis[j]=True
                color[j]=-c
                dfs(j,-c)
    for i in range(1,v+1):
        if not vis[i]:  
            vis[i]=True
            color[i]=1
            dfs(i,1)
    if flag:
        print('NO')
    else:
        print('YES')