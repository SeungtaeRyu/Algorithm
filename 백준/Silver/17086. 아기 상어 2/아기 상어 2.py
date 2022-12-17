import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

max_count = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            continue
        count = 1
        stack1 = [(i, j)]
        visited = [[0 for _ in range(m)] for _ in range(n)]
        visited[i][j] = 1

        while True:
            stack2 = []
            while stack1:
                x, y = stack1.pop()
                for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    nx = x + dx
                    ny = y + dy
                    if nx < 0 or nx == n or ny < 0 or ny == m or visited[nx][ny]:
                        continue
                    if arr[nx][ny] == 1:
                        break
                    else:
                        visited[nx][ny] = 1
                        stack2.append((nx, ny))
                else:
                    continue
                break
            else:
                if stack2:
                    stack1 = stack2[:]
                    count += 1
                    continue
                else:
                    break
            break

        max_count = max(max_count, count)
print(max_count)