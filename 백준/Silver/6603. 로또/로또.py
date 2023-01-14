def dfs(j):
    global arr
    if len(arr)==6:
        for i in arr:
            print(i,end=" ")
        print()
        return
    for i in range(j+1,lst[0]+1):
        arr.append(lst[i])
        dfs(i)
        arr.pop()
while True:
    lst = list(map(int,input().split()))
    if lst[0] == 0:
        break
    arr = []
    dfs(0)
    print()
