import sys
a = set()
b = set()
n,m = map(int,sys.stdin.readline().split())
for _ in range(n):
    a.add(sys.stdin.readline().rstrip())
for _ in range(m):
    b.add(sys.stdin.readline().rstrip())
ans = list(a&b)
ans.sort()
print(len(ans))
print(*ans,sep='\n') 