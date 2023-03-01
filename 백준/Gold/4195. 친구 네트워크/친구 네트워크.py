import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    relation_num = int(input())
    p = {}
    group = {}
    def find(x):
        if p[x]!=x:
            p[x] = find(p[x])
        return p[x]
    def union(a,b):
        a = find(a)
        b = find(b)
        if a < b:
            p[b] = a
            group[a]+=group[b]
            return group[a]
        else:
            p[a] = b
            group[b]+=group[a]
            return group[b]
    for __ in range(relation_num):
        p1,p2 = input().split()
        if p1 not in p:
            p[p1] = p1
            group[p1] = 1
        if p2 not in p:
            p[p2] = p2
            group[p2] = 1
        if find(p1)!=find(p2):
            print(union(p1,p2))
        else:
            print(group[find(p1)])