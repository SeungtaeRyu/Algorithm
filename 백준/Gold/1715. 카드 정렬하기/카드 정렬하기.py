import sys
import heapq
input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    heap.append(int(input()))
heapq.heapify(heap)

total = 0
while len(heap) > 1:
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    total += x+y
    heapq.heappush(heap, x+y)

print(total)