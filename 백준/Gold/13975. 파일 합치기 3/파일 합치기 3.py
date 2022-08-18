import heapq

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    heap = list(map(int, input().split()))
    heapq.heapify(heap)

    total = 0
    for _ in range(n-1):
        temp = 0
        temp += heapq.heappop(heap)
        temp += heapq.heappop(heap)
        heapq.heappush(heap, temp)
        total += temp
    print(total)