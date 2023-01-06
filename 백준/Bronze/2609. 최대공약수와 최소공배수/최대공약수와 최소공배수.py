a,b = map(int,input().split())
val = min(a,b)
x = 1
for i in range(2,val+1):
    if a%i == 0 and b%i == 0:
        x = i
print(x)
print((a*b)//x)