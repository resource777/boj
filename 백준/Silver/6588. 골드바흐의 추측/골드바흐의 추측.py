import sys

MAX = 1000000
prime = [-1]*(MAX+1)
for i in range(2,MAX+1):
    if prime[i] == -1:
        prime[i] = 1
        for j in range(2*i,MAX+1,i):       
            prime[j] = 0

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in range(3,n):
        if prime[i] == 1 and prime[n-i] == 1:
            print(n,"=",i,"+",(n-i))
            break