import sys, heapq
input = sys.stdin.readline
heap = []
for _ in range(int(input())):
    input_list = list(map(int, input().split()))
    if len(input_list) == 1:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(-1)
        pass
    else:
        for i in range(1, input_list[0]+1):
            heapq.heappush(heap, -input_list[i])