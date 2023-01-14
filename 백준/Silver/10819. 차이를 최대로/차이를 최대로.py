n = int(input())
lst = list(map(int,input().split()))
v = [False]*(n)
arr = []
ans = 0
def dfs():
    global ans
    if len(arr)==n:
        val = 0
        for i in range(n-1):
            val+=abs(arr[i]-arr[i+1])
        ans = max(ans,val)
        return
    for i in range(n):
        if not v[i]:
            arr.append(lst[i])
            v[i]=True
            dfs()
            arr.pop()
            v[i]=False
dfs()
print(ans)
