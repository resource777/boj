n = int(input())
DIV = 9901
dp = [[0]*3 for _ in range(n)]
dp[0][0]=1#nothing
dp[0][1]=1#left
dp[0][2]=1#right
for i in range(1,n):
    dp[i][0]=sum(dp[i-1])%DIV
    dp[i][1]=(dp[i-1][0]+dp[i-1][2])%DIV
    dp[i][2]=(dp[i-1][0]+dp[i-1][1])%DIV
print(sum(dp[n-1])%DIV)