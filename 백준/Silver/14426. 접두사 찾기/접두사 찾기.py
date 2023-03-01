import sys
input = sys.stdin.readline
n,m = map(int,input().split())
dic = {}
for _ in range(n):
    s = input().rstrip()
    tmp = dic
    for c in s:
        if c not in tmp:
            tmp[c] = {}
        tmp = tmp[c]
ans = 0
for _  in range(m):
    s = input().rstrip()
    tmp = dic
    flag = 1
    for c in s:
        if c not in tmp:
            flag = 0
            break
        else:
            tmp = tmp[c]
    if flag:
        ans+=1
print(ans)