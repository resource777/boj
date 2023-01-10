l,c = map(int,input().split())
lst = sorted(list(input().split()))
ans = []
def dfs(i):
    if len(ans)==l:
        mo=0
        for c in ans:
            if c in 'aeiou':
                mo+=1
        if mo>=1 and len(ans)-mo>=2:
            print(''.join(ans))
        return
    for j in range(i+1,len(lst)):
        ans.append(lst[j])
        dfs(j)
        ans.pop()
dfs(-1)
