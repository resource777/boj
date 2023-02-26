from collections import deque
t = int(input())
for _ in range(t):
    q = deque()
    store = int(input())
    v = [0]*store
    q.append(tuple(map(int,input().split())))
    lst = [tuple(map(int,input().split())) for __ in range(store)]
    goal = tuple(map(int,input().split()))
    flag = False
    while q:
        cx,cy = q.popleft()
        if abs(goal[0]-cx)+abs(goal[1]-cy)<=1000:
            print('happy')
            flag = True
            break
        for i in range(store):
            if abs(lst[i][0]-cx)+abs(lst[i][1]-cy)<=1000 and v[i]==0:
                q.append((lst[i][0],lst[i][1]))
                v[i]=1
    if not flag:
        print('sad')