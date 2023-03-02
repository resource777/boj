n,b = map(int,input().split())
m = [list(map(int,input().split())) for _ in range(n)]
def power(mat,b):
    if b == 1:
        tmp = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                tmp[i][j]= mat[i][j]%1000
        return tmp
    else:
        x = power(mat,b//2)
        tmp = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    tmp[i][j] = (tmp[i][j] + (x[i][k]*x[k][j])%1000)%1000
                tmp[i][j]%=1000
        if b%2==0:
            return tmp
        else:
            tmp2 = [[0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        tmp2[i][j] = (tmp2[i][j] + (tmp[i][k]*m[k][j])%1000)%1000
                    tmp2[i][j]%=1000
            return tmp2            
ans = power(m,b)
for i in ans:
    print(*i)  