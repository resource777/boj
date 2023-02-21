from collections import deque

def solution(maps):
    n=len(maps)
    m=len(maps[0])
    answer = 0
    q = deque()
    q.append((0,0,1))
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while q:
        cx,cy,ccan = q.popleft()
        if cx==n-1 and cy==m-1:
            answer=ccan
            break
        for i in range(4):
            nx,ny,ncan= dx[i]+cx,dy[i]+cy,ccan+1
            if 0<=nx<n and 0<=ny<m and maps[nx][ny]==1:
                q.append((nx,ny,ncan))
                maps[nx][ny] = 0
    if answer == 0:
        answer=-1
    return answer