n = int(input())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
a.append(a[0])
ans = 0
for i in range(n):
    ans += a[i][0]*a[i+1][1]-a[i+1][0]*a[i][1]
print(abs(round(ans/2,1)))