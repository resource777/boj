n,s  = map(int,input().split())
lst = list(map(int,input().split()))
arr = []
ans = 0
def dfs(i):
    global ans
    if i == n:
        if len(arr)>0 and sum(arr)==s:
            ans+=1
        return
    for j in range(i+1,n+1):
        if j==n:
            dfs(j)
            continue
        arr.append(lst[j])
        dfs(j)
        arr.pop()
dfs(-1)
print(ans)