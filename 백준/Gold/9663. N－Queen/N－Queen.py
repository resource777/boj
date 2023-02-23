n = int(input())
f = [0]*(n+1)
answer = 0
def dfs(x):
    global answer
    global f
    if x==n+1:
        answer+=1
        return
    for i in range(1,n+1):
        f[x] = i
        for j in range(1,x):
            if f[j]==i or abs(f[j]-i)==x-j:
                f[x]=16
                break
        if f[x]!=16:
            dfs(x+1)
dfs(1)
print(answer)
