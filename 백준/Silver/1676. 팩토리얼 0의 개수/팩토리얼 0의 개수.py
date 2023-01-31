ans = 0 
n = int(input())
two,five = 0,0
for i in range(2,n+1):
    while i%2==0:
        i//=2
        two+=1
    while i%5==0:
        i//=5
        five+=1
ans = min(two,five)
print(ans)
