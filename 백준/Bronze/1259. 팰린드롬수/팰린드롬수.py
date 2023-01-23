while True:
    x = int(input())
    if x==0:
        break
    x = str(x)
    for i in range(len(x)//2):
        if x[i] != x[len(x)-1-i]:
            print('no')
            break
    else:
        print('yes')