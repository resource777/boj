x = int(input())
g = [1]*1000001
for i in range(2,x+1):
    for j in range(i,x+1,i):
        g[j]+=i

print(sum(g[1:x+1]))