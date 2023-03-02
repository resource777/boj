import sys
import heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = 987654321
g = [[INF]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    g[i][i] = 0
for i in range(m):
    a,b,cost = map(int,input().split())
    g[a][b] = min(cost,g[a][b])
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            g[i][j] = min(g[i][j],g[i][k]+g[k][j])
for i in range(1,n+1):
    for j in range(1,n+1):
        if g[i][j]>=INF:
            print(0,end=' ')
        else:
            print(g[i][j],end=' ')
    print()
