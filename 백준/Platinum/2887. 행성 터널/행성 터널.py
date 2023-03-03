import sys
import heapq
input = sys.stdin.readline
n = int(input())
p = [i for i in range(n)]
def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]
def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b
xlst = []
ylst = []
zlst = []
for i in range(n):
    x,y,z = map(int,input().split())
    xlst.append((x,i))
    ylst.append((y,i))
    zlst.append((z,i))
xlst.sort()
ylst.sort()
zlst.sort()
q = []
for i in range(n-1):
    heapq.heappush(q,(abs(xlst[i][0]-xlst[i+1][0]),xlst[i][1],xlst[i+1][1]))
    heapq.heappush(q,(abs(ylst[i][0]-ylst[i+1][0]),ylst[i][1],ylst[i+1][1]))
    heapq.heappush(q,(abs(zlst[i][0]-zlst[i+1][0]),zlst[i][1],zlst[i+1][1]))
cnt = 0
ans = 0
while cnt < n-1:
    c,a,b = heapq.heappop(q)
    if find(a)!=find(b):
        union(a,b)
        cnt+=1
        ans+=c
print(ans)