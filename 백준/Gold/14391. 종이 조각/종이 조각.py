n,m = map(int,input().split())
f = [[i for i in input()] for _ in range(n)]
ans = 0

for i in range(1<<(n*m)):
    arr = []
    val = 0
    for j in range(n):
        tmp = ''
        for k in range(m):
            if i & (1<<(j*m+k)):
                tmp += f[j][k]
            else:
                if tmp!='':
                    val += int(tmp)
                    tmp=''
        if tmp!='':
            val += int(tmp)
    for j in range(m):
        tmp = ''
        for k in range(n):
            if not(i & (1<<(k*m+j))):
                tmp += f[k][j]
            else:
                if tmp!='':
                    val += int(tmp)
                    tmp=''
        if tmp!='':
            val += int(tmp)
    ans = max(ans,val)
print(ans)            