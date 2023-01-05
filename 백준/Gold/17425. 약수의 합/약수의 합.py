import sys

t = int(sys.stdin.readline().rstrip())
g = [1]*1000001
for i in range(2,1000001):
    for j in range(i,1000001,i):
        g[j]+=i
for i in range(2,1000001):
    g[i]+=g[i-1]
for _ in range(t):
    x = int(sys.stdin.readline().rstrip())
    print(g[x])