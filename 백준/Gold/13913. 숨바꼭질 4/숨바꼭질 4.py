from collections import deque

n,k = map(int,input().split())
v = [-1] * 100001
move = {}
q = deque([n])
v[n] = 0
move[n] = -1
while q:
    now = q.popleft()
    if now==k:
        break
    for next in [now*2,now-1,now+1]:
        if 0<=next<100001 and v[next] == -1:
            q.append(next)
            v[next] = v[now]+1
            move[next] = now
path = deque([k])
while move[path[0]]!=-1:
    x = move[path[0]]
    path.appendleft(x)
print(len(path)-1)
print(*path)