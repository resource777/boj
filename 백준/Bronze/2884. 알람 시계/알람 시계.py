h,m = map(int,input().split())
if h==0:
    if m<45:
        h,m=23,60-(45-m)
    else:
        m-=45
else:
    if m<45:
        h,m=h-1,60-(45-m)
    else:
        m-=45
print(h,m)