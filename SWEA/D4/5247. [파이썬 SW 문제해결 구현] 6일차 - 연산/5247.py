from collections import deque

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    maxsize = 2*m
    visited = [-1] * (maxsize + 1)

    q = deque()
    q.append(n)
    visited[n] = 0
    while q:
        if visited[m] != -1:
            break
        now_num = q.popleft()

        if 0 < now_num - 1 <= maxsize and visited[now_num - 1] == -1:
            visited[now_num - 1] = visited[now_num] + 1
            q.append(now_num - 1)
        if 0 < now_num + 1 <= maxsize and visited[now_num + 1] == -1:
            visited[now_num + 1] = visited[now_num] + 1
            q.append(now_num + 1)
        if 0 < now_num * 2 <= maxsize and visited[now_num * 2] == -1:
            visited[now_num * 2] = visited[now_num] + 1
            q.append(now_num * 2)
        if 0 < now_num - 10 <= maxsize and visited[now_num - 10] == -1:
            visited[now_num - 10] = visited[now_num] + 1
            q.append(now_num - 10)

    print(f'#{tc} {visited[m]}')
