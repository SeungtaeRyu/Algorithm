def rotate(query):
    sx, sy, ex, ey = query
    sx, sy, ex, ey = sx-1, sy-1, ex-1, ey-1
    temp = arr[sx][sy]
    temp_answer = [temp]

    # 위로 이동
    for x in range(sx, ex): # 1~3
        arr[x][sy] = arr[x+1][sy]
        temp_answer.append(arr[x][sy])
    # 왼쪽으로 이동
    for y in range(sy, ey): # 1~2
        arr[ex][y] = arr[ex][y+1]
        temp_answer.append(arr[ex][y])
    # 아래로 이동
    for x in range(ex, sx, -1): # 4~2
        arr[x][ey] = arr[x-1][ey]
        temp_answer.append(arr[x][ey])
    # 오른쪽으로 이동
    for y in range(ey, sy, -1): # 3~2
        arr[sx][y] = arr[sx][y-1]
        temp_answer.append(arr[sx][y])

    arr[sx][sy+1] = temp

    return min(temp_answer)


def solution(rows, columns, queries):
    global arr
    answer = []
    arr = []
    for i in range(rows):
        arr.append([j for j in range(1 + i * columns, 1 + i * columns + columns)])

    for query in queries:
        answer.append(rotate(query))

    return answer