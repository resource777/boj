import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
p = [0]*(n+1)
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

q = deque()
q.append(1)
p[1] = -1
while q:
    parent = q.popleft()
    for child in g[parent]:
        if p[child] == 0:
            p[child] = parent
            q.append(child)
for i in range(2,n+1):
    print(p[i])