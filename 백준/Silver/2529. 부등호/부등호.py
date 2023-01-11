n = int(input())
neq = list(input().split())
MAX = "0"
MIN = "9876543210"
v = [False]*10

def dfs(s,k):
    global MAX
    global MIN
    if len(s)==n+1:
        if int(MAX)<int(s):
            MAX = s
        if int(MIN)>int(s):
            MIN = s
        return
    for i in range(10):
        if not v[i] :
            if (neq[k]=='<' and s[k] < str(i)) or (neq[k]=='>' and s[k] >str(i)):
                v[i] = True
                dfs(s+str(i),k+1)
                v[i] = False
for i in '0123456789':
    v[int(i)]=True            
    dfs(i,0)    
    v[int(i)]=False
print(MAX)
print(MIN)
