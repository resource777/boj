n,k = map(int,input().split())
coin = [int(input()) for _ in range(n)]
coin.sort()
dp = [0]*(k+1)
for c in coin:
    if c<=k:
        dp[c] += 1
        for i in range(c+1,k+1):
            dp[i] += dp[i-c]
print(dp[k])

