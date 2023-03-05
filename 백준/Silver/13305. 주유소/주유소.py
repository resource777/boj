import sys
input = sys.stdin.readline
n = int(input())
dist = list(map(int,input().split()))
cost = list(map(int,input().split()))
ans = cost[0]*dist[0]
min_cost = cost[0]
for i in range(1,n-1):
    if min_cost>cost[i]:
        min_cost = cost[i]
    ans+=(min_cost*dist[i])
print(ans)