from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append((begin,0))
    while q:
        word,point = q.popleft()
        if word==target:
            answer=point
            break
        if point>len(words):
            break
        for w in words:
            cnt=0
            for i in range(len(w)):
                if w[i]!=word[i]:
                    cnt+=1
            if cnt==1:
                q.append((w,point+1))
    return answer