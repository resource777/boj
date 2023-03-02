import sys
import heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
g = [[] for _ in range(n+1)]
INF = 987654321
dist = [INF]*(n+1)
for i in range(m):
    a,b,cost = map(int,input().split())
    g[a].append((b,cost))
s,e = map(int,input().split())
q = []
heapq.heappush(q,(0,s))
dist[s] = 0
while q:
    d, now = heapq.heappop(q)
    if dist[now] < d:
        continue
    for i in range(len(g[now])):
        if dist[g[now][i][0]] > dist[now]+g[now][i][1]:
            dist[g[now][i][0]] = dist[now]+g[now][i][1]
            heapq.heappush(q,(dist[g[now][i][0]],g[now][i][0]))
print(dist[e])
