import sys
from collections import deque
input = sys.stdin.readline

def bfs(N, K):
    if N == K:
        return 0
    max_size = 100001
    visited = [-1] * max_size
    q = deque([N])
    visited[N] = 0
    while q:
        now_location = q.popleft()

        # 순간이동
        if now_location * 2 < max_size and visited[now_location*2] == -1:
            if now_location * 2 == K:
                return visited[now_location] + 1
            else:
                visited[now_location * 2] = visited[now_location] + 1
                q.append(now_location * 2)

        # X-1
        if now_location-1 >= 0 and visited[now_location-1] == -1:
            if now_location-1 == K:
                return visited[now_location]+1
            else:
                visited[now_location-1] = visited[now_location] + 1
                q.append(now_location-1)

        # X+1
        if now_location+1 < max_size and visited[now_location+1] == -1:
            if now_location+1 == K:
                return visited[now_location]+1
            else:
                visited[now_location+1] = visited[now_location] + 1
                q.append(now_location+1)


if __name__ == '__main__':
    n, k = map(int, input().split())
    print(bfs(n, k))