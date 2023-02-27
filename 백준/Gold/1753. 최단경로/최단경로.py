import sys
import heapq

input = sys.stdin.readline
vertex_num,edge_num = map(int,input().split())
start = int(input())
g = [[] for _ in range(vertex_num+1)]
INF = 987654321
dist = [INF]*(vertex_num+1)
for _ in range(edge_num):
    u,v,w = map(int,input().split())
    g[u].append((v,w))
q = []
q.append((0,start))
dist[start]=0
while q:
    d,v = heapq.heappop(q)
    if dist[v]<d:
        continue
    for adj in g[v]:
        if dist[adj[0]] > dist[v] + adj[1]:
            dist[adj[0]] = dist[v] + adj[1]
            heapq.heappush(q,(dist[adj[0]],adj[0]))
dist = dist[1:]
for i in dist:
    if i==INF:
        print('INF')
    else:
        print(i)