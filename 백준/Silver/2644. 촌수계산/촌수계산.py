n = int(input())
p1,p2 = map(int,input().split())
r = int(input())
g = [[] for _ in range(n+1)]
v = [0]*(n+1)
ans = 0
for _ in range(r):
    p,c = map(int,input().split())
    g[p].append(c)
    g[c].append(p)

def dfs(x,cnt):
    global ans
    if ans!=0:
        return
    v[x] = 1
    for i in g[x]:
        if v[i] == 0:
            dfs(i,cnt+1)
            if i==p2:
                ans=cnt+1
                return
dfs(p1,0)
if ans==0:
    ans-=1
print(ans)
