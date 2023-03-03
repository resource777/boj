import sys
input = sys.stdin.readline
n,s = map(int,input().split())
lst = list(map(int,input().split()))
for i in range(1,n):
    lst[i] += lst[i-1]
lst = [0] + lst
left = 1
right = 0
INF = 987654321
ans = INF
while left <= n and right <= n:
    if lst[left]-lst[right] >= s:
        ans = min(ans,left-right)
        right+=1
    else:
        left+=1
if ans == INF:
    print(0)
else:
    print(ans)