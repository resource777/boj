MAX = 1000000
prime = [-1]*(MAX+1)
m,n = map(int,input().split())
for i in range(2,MAX+1):
    if prime[i] == -1:
        prime[i] = 1
        for j in range(2*i,MAX+1,i):       
            prime[j] = 0
for j in range(m,n+1):
    if prime[j] == 1:
        print(j)