T = int(input())
for tc in range(1, T+1):
    n, m, k = map(int, input().split())

    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]

    info = []
    for i in range(k):
        x, y, ea, d = map(int, input().split())
        info.append((x, y, ea, d))

    for i in range(m):
        ea_arr = [[[] for _ in range(n)] for _ in range(n)]
        d_arr = [[[] for _ in range(n)] for _ in range(n)]
        while info:
            x, y, ea, d = info.pop()
            nx = x + dx[d]
            ny = y + dy[d]
            if nx == 0 or nx == n-1 or ny == 0 or ny == n-1:
                ea_arr[nx][ny].append(ea//2)
                d_arr[nx][ny].append(d+1 if d % 2 else d-1)
            else:
                ea_arr[nx][ny].append(ea)
                d_arr[nx][ny].append(d)

        for x in range(n):
            for y in range(n):
                if len(ea_arr[x][y]) == 0:
                    continue
                elif len(ea_arr[x][y]) == 1:
                    info.append((x, y, ea_arr[x][y][0], d_arr[x][y][0]))
                else:
                    sum_ea = sum(ea_arr[x][y])
                    d = d_arr[x][y][ea_arr[x][y].index(max(ea_arr[x][y]))]
                    info.append((x, y, sum_ea, d))
    total = 0
    for x, y, ea, d in info:
        total += ea

    print(f'#{tc} {total}')