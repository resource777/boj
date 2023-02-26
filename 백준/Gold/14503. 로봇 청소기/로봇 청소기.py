from collections import deque

n,m = map(int,input().split())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
r,c,d = map(int,input().split())
f = [list(map(int,input().split())) for _ in range(n)]
v = [[0]*m for _ in range(n)]

q = deque()
q.append((r,c,d))
clean=0
while q:
    cr,cc,cd = q.popleft()
    if v[cr][cc]==0:
        v[cr][cc]=1
        clean+=1
    dirty=0
    for k in range(4):
        nr,nc = cr+dx[k],cc+dy[k]
        if f[nr][nc]==0 and v[nr][nc]==0:
            dirty+=1
            break
    if dirty:
        for k in range(1,5):
            nd = (cd - k)%4
            nr,nc = cr+dx[nd],cc+dy[nd]
            if f[nr][nc]==0 and v[nr][nc]==0:
                q.append((nr,nc,nd))
                break
    else:
        nd = (cd + 2)%4
        nr,nc = cr+dx[nd],cc+dy[nd]
        if f[nr][nc]==1:
            break
        else:
            q.append((nr,nc,cd))
print(clean)
