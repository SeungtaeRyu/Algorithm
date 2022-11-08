import sys, heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

q = []
for i in range(m):
    heapq.heappush(q, (arr[0][i], 0, i))
    visited[0][i] = True

for i in range(1, n):
    heapq.heappush(q, (arr[i][0], i, 0))
    heapq.heappush(q, (arr[i][m-1], i, m-1))
    visited[i][0] = True
    visited[i][m-1] = True

count = 0
maxV = 0
while count < k:
    w, x, y = heapq.heappop(q)
    maxV = max(maxV, w)
    count += 1

    if x + 1 < n and visited[x + 1][y] == False:
        heapq.heappush(q, (arr[x + 1][y], x + 1, y))
        visited[x + 1][y] = True
    if x - 1 >= 0 and visited[x - 1][y] == False:
        heapq.heappush(q, (arr[x - 1][y], x - 1, y))
        visited[x - 1][y] = True
    if y + 1 < m and visited[x][y + 1] == False:
        heapq.heappush(q, (arr[x][y + 1], x, y + 1))
        visited[x][y + 1] = True
    if y - 1 >= 0 and visited[x][y - 1] == False:
        heapq.heappush(q, (arr[x][y - 1], x, y - 1))
        visited[x][y - 1] = True

print(maxV)