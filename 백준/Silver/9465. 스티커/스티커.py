import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [[0]*n for __ in range(2)]
    item = [list(map(int,input().split())) for __ in range(2)]
    dp[0][0] = item[0][0]
    dp[1][0] = item[1][0]
    if n>=2:
        dp[0][1] = item[0][1]+item[1][0]
        dp[1][1] = item[1][1]+item[0][0]
    for i in range(2,n):
        dp[0][i] = max(dp[1][i-1],dp[1][i-2])+item[0][i]
        dp[1][i] = max(dp[0][i-1],dp[0][i-2])+item[1][i]
    print(max(dp[0][n-1],dp[1][n-1]))