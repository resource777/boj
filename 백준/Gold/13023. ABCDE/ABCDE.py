import sys
n,m=map(int,sys.stdin.readline().split())
lst=[[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    lst[a].append(b)
    lst[b].append(a)
flag = False
def dfs(i,cnt,v):
    global flag
    if flag:
        return
    if cnt==5:
        flag = True
        return
    for j in lst[i]:
        if not v[j]:
            v[j]=True
            dfs(j,cnt+1,v)
            v[j]=False
for i in range(n):
    v = [False]*n
    if flag:
        print(1)
        break
    v[i]=True
    dfs(i,1,v)

if not flag:
    print(0)
