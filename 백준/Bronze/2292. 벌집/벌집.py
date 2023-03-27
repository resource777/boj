n = int(input())
steps = 1
start = 1
while start<n:
    start+=(6*steps)
    steps+=1
print(steps)