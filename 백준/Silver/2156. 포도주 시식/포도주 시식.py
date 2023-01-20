n = int(input())
dp = [0]*n
lst = [int(input()) for _ in range(n)]

if n>=1:
    dp[0]=lst[0]
if n>=2:
    dp[1]=lst[0]+lst[1]
if n>=3:
    dp[2]=max(max(lst[0]+lst[1],lst[0]+lst[2]),lst[1]+lst[2])
if n>=4:   
    for i in range(3,n):
        dp[i] = max(dp[i-2]+lst[i],dp[i-3]+lst[i-1]+lst[i],dp[i-1])
print(max(dp))