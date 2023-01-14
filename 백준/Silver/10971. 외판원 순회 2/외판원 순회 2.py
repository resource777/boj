n=int(input())
f = [list(map(int,input().split())) for _ in range(n)]
v = [False]*(n)
arr = []
ans = 987654321
def dfs():
    global ans
    if len(arr)==n:
        val = 0
        for i in range(n):
            if f[arr[i]][arr[(i+1)%n]] == 0:
                return
            val+=f[arr[i]][arr[(i+1)%n]]
        ans = min(val,ans)
        return
    for i in range(n):
        if not v[i]:
            v[i]=True
            arr.append(i)
            dfs()
            arr.pop()
            v[i]=False
dfs()
print(ans)