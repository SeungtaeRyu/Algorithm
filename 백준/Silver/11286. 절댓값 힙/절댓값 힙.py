import sys, heapq
input = sys.stdin.readline

q = []
for _ in range(int(input())):
    n = int(input())
    if n < 0:
        heapq.heappush(q, (-n, 1))
    elif n > 0:
        heapq.heappush(q, (n, 2))
    else:
        if q:
            num, buho = heapq.heappop(q)
            if buho == 1:
                print(-num)
            else:
                print(num)
        else:
            print(0)
