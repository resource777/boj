import sys
import heapq

input = sys.stdin.readline
vertex_num,edge_num = map(int,input().split())
g = [[] for _ in range(vertex_num+1)]
INF = 987654321
d1 = [INF]*(vertex_num+1)
d2 = [INF]*(vertex_num+1)
d3 = [INF]*(vertex_num+1)

for _ in range(edge_num):
    u,v,w = map(int,input().split())
    g[u].append((v,w))
    g[v].append((u,w))
a,b = map(int,input().split())
q1 = []
q2 = []
q3 = []

q1.append((0,1))
d1[1]=0
while q1:
    d,v = heapq.heappop(q1)
    if d1[v]<d:
        continue
    for adj in g[v]:
        if d1[adj[0]] > d1[v] + adj[1]:
            d1[adj[0]] = d1[v] + adj[1]
            heapq.heappush(q1,(d1[adj[0]],adj[0]))

q2.append((0,a))
d2[a]=0
while q2:
    d,v = heapq.heappop(q2)
    if d2[v]<d:
        continue
    for adj in g[v]:
        if d2[adj[0]] > d2[v] + adj[1]:
            d2[adj[0]] = d2[v] + adj[1]
            heapq.heappush(q2,(d2[adj[0]],adj[0]))

q3.append((0,b))
d3[b]=0
while q3:
    d,v = heapq.heappop(q3)
    if d3[v]<d:
        continue
    for adj in g[v]:
        if d3[adj[0]] > d3[v] + adj[1]:
            d3[adj[0]] = d3[v] + adj[1]
            heapq.heappush(q3,(d3[adj[0]],adj[0]))
#123n
#132n
#1232n
#1323n
#1-2,3
#2-3,n
#3-2,n
n = vertex_num
ans = INF
if d1[a]+d2[b]+d3[n] < ans:
    ans = d1[a]+d2[b]+d3[n]
if d1[b]+d3[a]+d2[n] < ans:
    ans = d1[b]+d3[a]+d2[n]
if d1[a]+d2[b]+d3[a]+d2[n] < ans:
    ans = d1[a]+d2[b]+d3[a]+d2[n]
if d1[b]+d3[a]+d2[b]+d3[n] < ans:
    ans = d1[b]+d3[a]+d2[b]+d3[n]
if ans==INF:
    print(-1)
else:
    print(ans)