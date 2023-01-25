import sys
from collections import deque

n=int(sys.stdin.readline())
q=deque()
for _ in range(n):
    line = sys.stdin.readline().split()
    if len(line) == 1:
        if line[0] == 'front':
            if len(q):  
                print(q[0])
            else:
                print(-1)
        elif line[0] == 'back':
            if len(q):  
                print(q[-1])
            else:
                print(-1)
        elif line[0] == 'size':
            print(len(q))
        elif line[0] == 'empty':
            if len(q):
                print(0)
            else:
                print(1)
        elif line[0] == 'pop_front':
            if len(q):  
                print(q.popleft())
            else:
                print(-1)
        elif line[0] == 'pop_back':
            if len(q):  
                print(q.pop())
            else:
                print(-1)
    elif len(line)==2:
        if line[0]=='push_front':
            q.appendleft(int(line[1]))
        elif line[0]=='push_back':
            q.append(int(line[1]))