n = int(input())
lst = list(map(int,input().split()))
last_inc_idx = -1
for i in range(len(lst)-1):
    if lst[i] < lst[i+1]:
        last_inc_idx = i
if last_inc_idx == -1:
    print(-1)
else:
    if last_inc_idx+1 == len(lst)-1:
        lst[last_inc_idx],lst[last_inc_idx+1] = lst[last_inc_idx+1],lst[last_inc_idx]
    else:
        num = last_inc_idx+1
        for i in range(last_inc_idx+1,len(lst)):
            if lst[i] > lst[last_inc_idx] and lst[i]<lst[num]:
                num = i
        lst[last_inc_idx],lst[num] = lst[num],lst[last_inc_idx]
        lst[last_inc_idx+1:] = sorted(lst[last_inc_idx+1:])
    for i in range(len(lst)):
        print(lst[i],end=" ")