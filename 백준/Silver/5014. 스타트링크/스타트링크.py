from collections import deque
f,s,g,u,d = map(int,input().split())
q = deque()
q.append((s,0))
v = [-1]* (f+1)

v[s]=0
while q:
    cpos, ctouch = q.popleft()
    if cpos == g:
        print(ctouch)
        exit(0)
    if u!=0 and cpos+u<=f and v[cpos+u]==-1:
        q.append((cpos+u,ctouch+1))
        v[cpos+u]=ctouch+1
    if d!=0 and cpos-d>=1 and v[cpos-d]==-1:
        q.append((cpos-d,ctouch+1))
        v[cpos-d]=ctouch+1
print('use the stairs')
