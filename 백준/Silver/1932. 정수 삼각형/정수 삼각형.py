n = int(input())
dp = [list(map(int,input().split())) for _ in range(n)]
for i in range(1,n):
    for j in range(i+1):
        val=0
        for k in [0,-1]:
            if j+k>=0 and j+k<=i-1:
                val = max(val,dp[i-1][j+k])
        dp[i][j] +=val
print(max(dp[n-1]))