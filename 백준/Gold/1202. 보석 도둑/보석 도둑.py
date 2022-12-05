import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())

je = []
ga = []
for i in range(n):
    je.append(tuple(map(int, input().split())))

for i in range(k):
    ga.append(int(input()))

je.sort(key=lambda x: x[0])
ga.sort()
can = []

total = 0
index = 0
for gabang in ga:
    while index < n and gabang >= je[index][0]:
        heapq.heappush(can, -je[index][1])
        index += 1
    if can:
        total -= heapq.heappop(can)
print(total)