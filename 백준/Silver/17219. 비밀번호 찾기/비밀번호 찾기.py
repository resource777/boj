import sys
n,m = map(int,sys.stdin.readline().split())
dic = {}
for _ in range(n):
    url,password = sys.stdin.readline().split()
    dic[url] = password
for _ in range(m):
    find = sys.stdin.readline().rstrip()
    print(dic[find])