e,s,m = map(int,input().split())
e-=1
s-=1
m-=1
year = 0
while True:
    if year%15 == e and year%28 == s and year%19 == m:
        break
    year+=1
print(year+1)

