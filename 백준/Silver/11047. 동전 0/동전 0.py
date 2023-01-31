n,k = map(int,input().split())
coin = []
for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)
ans = 0
for i in range(n):
    if coin[i]<=k:
        ans+=k//coin[i]
        k%=coin[i]
print(ans)