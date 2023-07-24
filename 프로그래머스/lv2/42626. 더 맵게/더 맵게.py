import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while True:
        try :
            if scoville[0] >= K:
                break
            x = heapq.heappop(scoville)  
            y = heapq.heappop(scoville)
            heapq.heappush(scoville, x+y*2)
            answer += 1
        except:
            return -1
    
    return answer