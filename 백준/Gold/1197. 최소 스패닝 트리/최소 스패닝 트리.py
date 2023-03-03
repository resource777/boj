import sys
import heapq
input = sys.stdin.readline
v,e = map(int,input().split())
p = [i for i in range(v+1)]
def find(x):
    if p[x]!=x:
        p[x] = find(p[x])
    return p[x]
def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        p[b] = a
    else:
        p[a] = b
q = []
for i in range(e):
    a,b,cost = map(int,input().split())
    heapq.heappush(q,(cost,a,b))
cnt = 0
ans = 0
while cnt < v-1:
    c,a,b = heapq.heappop(q)
    if find(a)!=find(b):
        union(a,b)
        cnt+=1
        ans+=c
print(ans)