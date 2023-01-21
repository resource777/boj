n = int(input())
for _ in range(n):
    t,s = input().split()
    for i in s:
        print(i*int(t),end='')
    print()
    