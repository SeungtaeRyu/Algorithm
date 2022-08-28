import sys, heapq
input = sys.stdin.readline

start_list = []
end_list = []
for _ in range(int(input())):
    __, start, end = map(int, input().split())
    start_list.append(start)
    end_list.append(end)
heapq.heapify(start_list)
heapq.heapify(end_list)

count = 0
max_count = 0
while start_list:
    x = start_list[0]
    y = end_list[0]
    if x < y:
        count += 1
        max_count = max(count, max_count)
        heapq.heappop(start_list)
    else:
        count -= 1
        heapq.heappop(end_list)
print(max_count)