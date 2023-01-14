n = int(input())

v = [False]*(n+1)
arr = []
def dfs():
    if len(arr)==n:
        for i in arr:
            print(i,end=" ")
        print()
        return
    for i in range(1,n+1):
        if not v[i]:
            arr.append(i)
            v[i]=True
            dfs()
            arr.pop()
            v[i]=False
dfs()
