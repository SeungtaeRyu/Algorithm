import heapq

heap = []
result = []
for i in range(int(input())):
    x = int(input())
    if x > 0:
        heapq.heappush(heap, x)
    else:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)

for data in result:
    print(data)