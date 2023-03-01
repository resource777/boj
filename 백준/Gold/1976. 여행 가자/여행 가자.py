total_num = int(input())
included_num = int(input())
g = []
for _ in range(total_num):
    g.append(list(map(int,input().split())))
included_city = list(map(int,input().split()))
for i in range(included_num):
    included_city[i]-=1
p = [i for i in range(total_num)]
def find(a):
    if p[a] != a:
        p[a] = find(p[a])
    return p[a]
def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b
for i in range(total_num):
    for j in range(i+1,total_num):
        if g[i][j]==1:
            union(i,j)
for i in range(1,included_num):
    if find(included_city[i])!=find(included_city[0]):
        print('NO')
        exit(0)
print('YES')