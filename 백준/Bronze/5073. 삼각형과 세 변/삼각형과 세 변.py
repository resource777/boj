while True:
    a,b,c = map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    s = []
    s.append(a)
    s.append(b)
    s.append(c)
    s.sort()
    if s[2] >= s[0]+s[1]:
        print('Invalid')
    else:
        s = set(s)
        if len(s) == 3:
            print('Scalene')
        elif len(s) == 2:
            print('Isosceles')
        else:
            print('Equilateral')