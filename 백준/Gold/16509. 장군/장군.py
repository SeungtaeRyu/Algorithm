from collections import deque

sr, sc = map(int, input().split())
kr, kc = map(int, input().split())

visited = [[-1 for _ in range(9)] for _ in range(10)]
directions = [(-3, -2), (-3, 2), (-2, -3), (-2, 3), (2, -3), (2, 3), (3, -2), (3, 2)]
isCheck = [[(-2, -1), (-1, 0)], [(-2, 1), (-1, 0)], [(-1, -2), (0, -1)], [(-1, 2), (0, 1)],
           [(1, -2), (0, -1)], [(1, 2), (0, 1)], [(2, -1), (1, 0)], [(2, 1), (1, 0)], ]

visited[sr][sc] = 0
stack = deque([(sr, sc)])

while stack:
    x, y = stack.popleft()
    for i in range(8):
        nx = x + directions[i][0]
        ny = y + directions[i][1]

        if nx < 0 or nx >= 10 or ny < 0 or ny >= 9 or visited[nx][ny] != -1:
            continue
        if x + isCheck[i][0][0] == kr and y + isCheck[i][0][1] == kc:
            continue
        if x + isCheck[i][1][0] == kr and y + isCheck[i][1][1] == kc:
            continue

        visited[nx][ny] = visited[x][y] + 1
        stack.append((nx, ny))
        if nx == kr and ny == kc:
            print(visited[nx][ny])
            exit()
print(-1)