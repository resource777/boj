import sys
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
dp = [0]*n
dp[0] = lst[0]
for i in range(1,n):
    dp[i] = max(lst[i],dp[i-1]+lst[i])
print(max(dp))