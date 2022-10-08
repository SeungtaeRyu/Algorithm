import sys
input = sys.stdin.readline

R, C, m = map(int, input().split())

info = []
for _ in range(m):
    info.append(tuple(map(int, input().split())))

total = 0
for i in range(1, C+1):
    if not info:
        break

    minV = 1000
    for j in range(len(info)):
        if info[j][1] == i:
            if minV > info[j][0]:
                minV = info[j][0]
                find = j

    if minV != 1000:
        total += info[find][4]
        info.pop(find)

    arr_s = [[[] for _ in range(C+1)] for _ in range(R+1)]
    arr_d = [[[] for _ in range(C+1)] for _ in range(R+1)]
    arr_z = [[[] for _ in range(C+1)] for _ in range(R+1)]
    for r, c, s, d, z in info:
        # 위
        if d == 1:
            if r-s <= 1:
                ss = s-(r-1)
                a = ss // (R-1)
                b = ss % (R-1)

                if a % 2 == 0:
                    r = b+1
                    d = 2
                else:
                    r = R-b
            else:
                r = r-s
                if r == 1:
                    d = 2

        # 아래
        elif d == 2:
            if r+s >= R:
                ss = s-(R-r)
                a = ss // (R-1)
                b = ss % (R-1)

                if a % 2 == 0:
                    r = R-b
                    d = 1
                else:
                    r = b+1
            else:
                r = r+s
                if r == R:
                    d = 1

        # 오른
        elif d == 3:
            if c+s >= C:
                ss = s-(C-c)
                # print(s)
                a = ss // (C-1)
                b = ss % (C-1)
                # print(f'a={a} b={b}')
                if a % 2 == 0:
                    c = C-b
                    d = 4
                else:
                    c = b+1
            else:
                c = c+s
                if c == C:
                    d = 4

        # 왼
        elif d == 4:
            if c - s <= 1:
                ss = s - (c - 1)
                a = ss // (C - 1)
                b = ss % (C - 1)

                if a % 2 == 0:
                    c = b + 1
                    d = 3
                else:
                    c = C - b
            else:
                c = c - s
                if c == 1:
                    d = 3

        arr_s[r][c].append(s)
        arr_d[r][c].append(d)
        arr_z[r][c].append(z)

    info = []
    for i in range(1, R+1):
        for j in range(1, C+1):
            if len(arr_s[i][j]) == 0:
                continue
            elif len(arr_s[i][j]) == 1:
                info.append((i, j, arr_s[i][j][0], arr_d[i][j][0], arr_z[i][j][0]))
            else:
                k = arr_z[i][j].index(max(arr_z[i][j]))
                info.append((i, j, arr_s[i][j][k], arr_d[i][j][k], arr_z[i][j][k]))

print(total)
