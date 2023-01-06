h = [int(input()) for _ in range(9)]
for i in range(9):
    for j in range(i+1,9):
        tmp1,tmp2 = h[i], h[j]
        h[i],h[j] = 0, 0
        if sum(h) == 100:
            h = sorted(h)
        else:
            h[i],h[j] = tmp1,tmp2
for i in range(2,9):
    print(h[i])
