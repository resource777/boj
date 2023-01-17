n = int(input())
lst = list(map(int,input().split()))
dp = [1]*n
idx = [0]*n
for i in range(1,n):
    for j in range(i):
        if lst[j] < lst[i] and dp[i]<dp[j]+1:
            dp[i] = dp[j]+1
            idx[i] = idx[j]+1
len = max(dp)
print(len)
tmp = []
for i in range(n-1,-1,-1):
    if len-1 == idx[i]:
        tmp.append(lst[i])
        len-=1
for i in range(max(dp)-1,-1,-1):
    print(tmp[i],end=" ")