import sys
sys.stdin = open("input.txt")

from collections import deque

def bfs(x, y):
    visited[x][y] =True
    q = deque([(x, y)])
    while q:
        # queue의 제일 왼쪽을 꺼내 인접 4곳을 조사
        now = q.popleft()
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx = now[0] + dx
            ny = now[1] + dy
            # 인접하는 점이 맵을 벗어나거나 방문했거나 길이 막혀있으면 안감
            if nx < 0 or nx >= 16 or ny < 0 or ny >= 16 or visited[nx][ny] or arr[nx][ny] == '1':
                continue
            # 인접하는 점의 값이 3이면 1을 반환하며 함수를 종료
            elif arr[nx][ny] == '3':
                return 1
            # 위의 두 조건이 아니면 queue에 다음 지점을 push하고, 방문기록을 저장.
            else:
                q.append((nx, ny))
                visited[nx][ny] = True
    # queue가 비어졌는데도(=갈수 있는 길의 완전탐색을 끝냈는데도)
    # while문 안의 return을 못만나면 3으로 가는 길이 없다는 뜻! 0을 반환하며 함수를 종료
    return 0

for _ in range(10):
    tc = input()
    # 맵, 방문기록 초기화
    arr = [list(input()) for _ in range(16)]
    visited = [[False for _ in range(16)] for _ in range(16)]

    # 시작 인덱스 찾기
    for i in range(16):
        for j in range(16):
            if arr[i][j] == '2':
                x, y = i, j

    print(f'#{tc} {bfs(x, y)}')
