import heapq

def solution(scoville, K):
    answer = 0
    hq = []
    for item in scoville:
        heapq.heappush(hq,item)
    for i in range(len(scoville)):
        if hq[0]>=K:
            return answer
        else:
            if len(hq)>=2:
                answer+=1
                x = heapq.heappop(hq)
                y = heapq.heappop(hq)
                heapq.heappush(hq,x+y*2)
            else:
                answer=-1
                break
    return answer