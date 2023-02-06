n,m,r = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
f = [[0]*max(n,m) for _ in range(max(n,m))]
oper = list(map(int,input().split()))
for i in range(n):
    for j in range(m):
        f[i][j] = lst[i][j]
def func1():
    for i in range(n//2):
        for j in range(m):
            f[i][j],f[n-1-i][j] = f[n-1-i][j],f[i][j]  
def func2():
    for i in range(n):
        for j in range(m//2):
            f[i][j],f[i][m-1-j] = f[i][m-1-j],f[i][j]  
def func3():
    rotate()
def func4():
    rotate()
    rotate()
    rotate()
def func5():
    minif = [[[0]*(m//2) for _ in range(n//2)] for __ in range(4)]
    dx = [0,0,1,1]
    dy = [0,1,1,0]
    for k in range(4):
        for i in range(n//2):
            for j in range(m//2):
                minif[k][i][j] = f[i+dx[k]*(n//2)][j+dy[k]*(m//2)]
    for k in range(4):
        for i in range(n//2):
            for j in range(m//2):
                f[i+dx[(k+1)%4]*(n//2)][j+dy[(k+1)%4]*(m//2)] = minif[k][i][j]
    
def func6():
    func5()
    func5()
    func5()
def rotate():
    global n,m
    temp = [[0]*max(n,m) for _ in range(max(n,m))]
    for i in range(max(n,m)):
        for j in range(max(n,m)):
            temp[i][j] = f[j][i]
    for i in range(max(n,m)):
        for j in range(max(n,m)):
            f[i][j] = temp[i][j]
    n,m = m,n
    func2()

for l in oper:
    if l==1:
        func1()
    elif l==2:
        func2()
    elif l==3:
        func3()
    elif l==4:
        func4()
    elif l==5:
        func5()
    elif l==6:
        func6()
for i in range(n):
    for j in range(m):
        print(f[i][j],end=" ")
    print()
