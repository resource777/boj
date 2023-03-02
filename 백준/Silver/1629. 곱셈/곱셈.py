a,b,c = map(int,input().split())
def power(a,b):
    if b == 1:
        return a%c
    else:
        if b%2==0:
            return power(a,b//2)**2%c
        else:
            return ((power(a,b//2)**2%c)*a)%c
print(power(a,b))