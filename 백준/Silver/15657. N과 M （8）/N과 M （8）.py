n,m = map(int, input().split())
arr = sorted(list(map(int,input().split())))
tmp = []
def dfs(k):
    if len(tmp)==m:
        for i in tmp:
            print(i,end=" ")
        print()
        return
    for i in range(k,len(arr)):
        tmp.append(arr[i])
        dfs(i)
        tmp.pop()
dfs(0)
