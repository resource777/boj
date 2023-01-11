n = int(input())
line = input()
f = [[0 for __ in range(n)] for _ in range(n)]
k=0
arr = [0] * 10
for i in range(n):
    for j in range(i,n):
        f[i][j]=line[k]
        k+=1
find = False
def dfs(i):
    global find
    global arr
    global v
    if find:
        return
    if i==-1:
        find = True
        for j in range(n):
            print(arr[j],end=" ")
        return
    if f[i][i] == '0':
        dfs(i-1)
        
    elif f[i][i] == '-':
        for j in range(-10,0):
            val = j
            can = True
            for k in range(i+1,n):
                val += arr[k]
                if not((val<0 and f[i][k]=='-') or (val>0 and f[i][k]=='+') or (val==0 and f[i][k]=='0')):
                    can = False
                    break
            if can:
                arr[i] = j
                dfs(i-1)
    elif f[i][i] == '+':
        for j in range(1,11):
            val = j
            can = True
            for k in range(i+1,n):
                val += arr[k]
                if not((val<0 and f[i][k]=='-') or (val>0 and f[i][k]=='+') or (val==0 and f[i][k]=='0')):
                    can = False
                    break
            if can:
                arr[i] = j
                dfs(i-1)
dfs(n-1)