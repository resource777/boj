a,b = map(int,input().split())
x,y = max(a,b),min(a,b)
while y!=0:
    x,y = y,x%y
print(x)
print(a*b//x)
