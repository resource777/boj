n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
ans = []
max_val = 0
def cal(i):
    global max_val
    if i==n:
        val=0
        ans.append((n,0,0))
        for j in range(len(ans)-1):
            if ans[j][0]+ans[j][1]-1>=ans[j+1][0]:
                ans.pop()
                return
            val+=ans[j][2]
        if max_val < val:
            max_val = val
        ans.pop()
        return
    ans.append((i,lst[i][0],lst[i][1]))
    cal(i+1)
    ans.pop()
    cal(i+1)
cal(0)
print(max_val)