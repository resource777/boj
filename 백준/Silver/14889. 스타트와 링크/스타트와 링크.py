n = int(input())
f = [list(map(int,input().split())) for _ in range(n)]
sum=0
arr = []
ans = 40000
def dfs(i):
    global ans
    if len(arr)==(n//2):
        val=0
        val2=0
        tmp=[]
        for j in range(n):
            if j not in arr:
                tmp.append(j)
        for j in range(n//2):
            for k in range(j+1,n//2):
                val+=f[arr[j]][arr[k]]+f[arr[k]][arr[j]]
                val2+=f[tmp[j]][tmp[k]]+f[tmp[k]][tmp[j]]
        ans = min(ans,abs(val-val2))
        return
    for j in range(i+1,n):
        arr.append(j)
        dfs(j)
        arr.pop()
dfs(-1)
print(ans)        