n,m = map(int,input().split())
arr = []

def dfs(k):
    if len(arr)==m:
        for i in arr:
            print(i,end=" ")
        print()
        return
    for i in range(k,n+1):
        arr.append(i)
        dfs(i)
        arr.pop()
dfs(1)