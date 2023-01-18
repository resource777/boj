t = int(input())
MAX = 1000000009
dp = [[0]*4 for _ in range(1000001)]
dp[1][1]=1
dp[1][0]=1
dp[2][1]=1
dp[2][2]=1
dp[2][0]=2
dp[3][1]=sum(dp[2][1:])
dp[3][2]=sum(dp[1][1:])
dp[3][3]=1
dp[3][0]=sum(dp[3])
for i in range(4,1000001):
    dp[i][1]= dp[i-1][0]
    dp[i][2]= dp[i-2][0]
    dp[i][3]= dp[i-3][0]
    dp[i][0]= sum(dp[i])%MAX
for _ in range(t):
    print(dp[int(input())][0])