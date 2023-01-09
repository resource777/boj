n,m = map(int, input().split())
arr = sorted(list(map(int,input().split())))
tmp = []
def dfs():
    if len(tmp)==m:
        for i in tmp:
            print(i,end=" ")
        print()
        return
    for i in range(len(arr)):
        tmp.append(arr[i])
        dfs()
        tmp.pop()
dfs()
