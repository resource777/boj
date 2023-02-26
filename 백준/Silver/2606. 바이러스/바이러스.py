n = int(input())
edge_num = int(input())
g = [[] for _ in range(n+1)]
v = [0]*(n+1)
for _ in range(edge_num):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
answer=0
def dfs(x):
    global answer
    v[x]=1
    for i in g[x]:
        if v[i]==0:
            answer+=1
            dfs(i)
dfs(1)
print(answer)