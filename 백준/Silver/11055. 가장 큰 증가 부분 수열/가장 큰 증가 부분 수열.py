n = int(input())
lst = list(map(int,input().split()))
dp = [0]*n
dp[0] = lst[0]
for i in range(1,n):
    dp[i] = lst[i]
    for j in range(i):
        if lst[j]<lst[i]:
            dp[i] = max(dp[i],dp[j]+lst[i])
print(max(dp))