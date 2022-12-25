import sys
input = sys.stdin.readline

def f(x, y, ans):
    if len(ans) == 6:
        ans_set.add(ans)
        return

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx == 5 or ny == 5:
            continue
        else:
            f(nx, ny, ans + arr[nx][ny])

arr = [list(map(str, input().split())) for _ in range(5)]
ans_set = set()

for i in range(5):
    for j in range(5):
        f(i, j, arr[i][j])

print(len(ans_set))