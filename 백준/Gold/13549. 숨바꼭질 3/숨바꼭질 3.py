from collections import deque
n,k = map(int,input().split())
v = [-1]*100001
q = deque([n])
v[n] = 0

while q:
    cur = q.popleft()
    if cur==k:
        break
    for next in [cur-1,cur+1,cur*2]:
        if 0<=next<100001 and v[next]==-1:
            if next==cur*2:
                q.appendleft(next)
                v[next]=v[cur]
            else:
                q.append(next)
                v[next]=v[cur]+1
print(v[k])