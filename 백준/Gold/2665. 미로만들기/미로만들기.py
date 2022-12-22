import sys, heapq
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]

visited = [[0 for _ in range(n)] for _ in range(n)]
stack = []
heapq.heappush(stack, (0, 0, 0))

while True:
    c, x, y = heapq.heappop(stack)

    if x == n-1 and y == n-1:
        print(c)
        break

    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
            continue
        visited[nx][ny] = 1
        if arr[nx][ny] == 1:
            heapq.heappush(stack, (c, nx, ny))
        else:
            heapq.heappush(stack, (c+1, nx, ny))
