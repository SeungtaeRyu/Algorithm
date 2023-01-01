import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

count = 0
q1 = []
q2 = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q2.append((i, j))
            visited[i][j] = 1
        if arr[i][j] == -1:
            visited[i][j] = 1

while q2:
    q1 = q2[:]
    q2 = []
    while q1:
        x, y = q1.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
                continue
            visited[nx][ny] = 1
            arr[nx][ny] = 1
            q2.append((nx, ny))
    count += 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(-1)
            exit()

print(count-1)