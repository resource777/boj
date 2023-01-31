import sys
n,m = map(int,sys.stdin.readline().split())
dic = {}
dic2 = {}
for i in range(1,n+1):
    name = sys.stdin.readline().rstrip()
    dic[name] = i
    dic2[i] = name
for _ in range(m):
    s = sys.stdin.readline().rstrip()
    if s.isalpha():
        print(dic[s])
    else:
        print(dic2[int(s)])