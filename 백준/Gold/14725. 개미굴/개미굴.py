n = int(input())
root = {}
for _ in range(n):
    line = list(input().split())
    k = int(line[0])
    line = line[1:]
    x = root
    for i in range(k):
        if line[i] not in x:
            x[line[i]] = {}
        x = x[line[i]]
root = dict(sorted(root.items()))
def print_func(d,dep):
    for i in d.keys():
        for _ in range(dep*2):
            print('-',end='')
        print(i)
        if d[i]:
            d[i] = dict(sorted(d[i].items()))
            print_func(d[i],dep+1)
print_func(root,0)