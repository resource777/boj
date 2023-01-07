n = int(input())
ans = abs(n-100)
key = [1]*10
crushed = int(input())
if crushed:
    for i in list(map(int,input().split())):
        key[i] = 0
for i in range(1000000):
    itoa = str(i)
    press = True
    for j in itoa:
        if key[int(j)] == 0:
            press = False
            break
    if not press:
        continue
    if ans > len(itoa)+abs(i-n):
        ans = min(len(itoa)+abs(i-n),ans)
print(ans)