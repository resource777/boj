from collections import deque

s = int(input())
v = [[-1]*2001 for _ in range(2001)]
q = deque()#(화면,클립보드)
q.append((1,0))
v[1][0] = 0

while q:
    disp,clip = q.popleft()
    if disp==s:
        print(v[disp][clip])
        break
    for (d,c) in [(disp,disp),(disp+clip,clip),(disp-1,clip)]:
        if 0<=d<2001 and 0<=c<2001 and v[d][c] == -1:
            v[d][c] = v[disp][clip]+1
            q.append((d,c))