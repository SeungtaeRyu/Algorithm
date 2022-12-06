import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

q = []
for i in range(n-1):
    heapq.heappush(q, nums[i]-nums[i+1])

total = -sum(q)
for i in range(k-1):
    total += heapq.heappop(q)
print(total)