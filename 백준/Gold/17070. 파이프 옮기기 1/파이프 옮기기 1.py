n = int(input())
f = [list(map(int,input().split())) for _ in range(n)]
dp = [[[0]*(n+1) for _ in range(n+1)] for __ in range(3)]
# 0 가로, 1 세로, 2 대각선
dp[0][1][2] = 1
for i in range(1,n+1):
    for j in range(2,n+1):
        if i==1 and j==2:
            continue
        if f[i-1][j-1]==0:
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]
            if f[i-1][j-2] == 0 and f[i-2][j-1] == 0:
                dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
# for i in range(3):
#     for j in range(1,n+1):
#         for k in range(1,n+1):
#             print(dp[i][j][k], end=' ')
#         print()
#     print()
print(dp[0][n][n]+dp[1][n][n]+dp[2][n][n])
