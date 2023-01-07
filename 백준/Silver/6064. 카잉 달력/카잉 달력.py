import sys

t = int(sys.stdin.readline())
def gcd(a,b):
    a,b = max(a,b),min(a,b)
    while b != 0:
        a,b = b,a%b
    return a

for _ in range(t):
    n,m,x,y = map(int,sys.stdin.readline().split())
    g = gcd(n,m)
    l = (n*m)//g
    start = x
    find = False
    while start <= l:
        if (start-1)%m + 1 == y:
            print(start)
            find = True
        start+=n
    if not find:
        print(-1)