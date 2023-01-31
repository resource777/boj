n = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans = 0
for i in range(n):
    ans += (n-i)*lst[i]
print(ans)