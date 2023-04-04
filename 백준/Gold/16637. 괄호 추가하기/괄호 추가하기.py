n = int(input())
s = input().rstrip()
ans = -(2**31)

def cal(op,v1,v2):
    if op=='*':
        return v1*v2
    elif op=='+':
        return v1+v2
    elif op=='-':
        return v1-v2
    
def dfs(idx, val):

    global ans
    if idx == n-1:
        ans = max(ans,val)
        return
    
    if idx+2 < n:
        dfs(idx+2,cal(s[idx+1],val,int(s[idx+2])))
    if idx+4 < n:
        dfs(idx+4,cal(s[idx+1],val,cal(s[idx+3],int(s[idx+2]),int(s[idx+4]))))

dfs(0,int(s[0]))
print(ans)