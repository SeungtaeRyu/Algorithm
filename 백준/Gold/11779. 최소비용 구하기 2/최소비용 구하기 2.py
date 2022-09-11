import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

adj = {i: [] for i in range(n+1)}                   # adj 행렬 초기화
routes = {i: [] for i in range(n+1)}
for _ in range(m):
    x, y, p = map(int, input().split())
    adj[x].append((y, p))

# print()
# print(adj)

dp = [sys.maxsize] * (n+1)                                  # dp 초기화
visited = [False] * (n+1)                           # visit 초기화

start, end = map(int, input().split())              # 시작점, 끝점 세팅

stack = [start]                                                     # 시작점을 스택에 넣고 시작
dp[start] = 0                                                       # 시작점 거리 비용 0으로 설정
routes[start].append(start)
while stack:
    now_node = stack.pop()                                          # 스택에 있는 노드를 pop 하고 "방문기록 체크"
    visited[now_node] = True
    for next_node, next_price in adj[now_node]:                                 # pop 한 노드에서 갈 수 있는 다음 노드 탐색 및 비용 계산
        if visited[next_node]:
            continue
        else:
            # routes[next_node] = routes[now_node] + [next_node]
            if dp[now_node] + next_price < dp[next_node]:
                dp[next_node] = dp[now_node] + next_price
                routes[next_node] = routes[now_node] + [next_node]
            # dp[next_node] = min(dp[now_node] + next_price, dp[next_node])

    # print(visited)
    # print(dp)

    next_index = 0                      # 방문한 노드를 제외하고 비용이 가장 적은 노드를 next 노드로 설정하기 위해 인덱스를 찾음
    min_value = sys.maxsize
    for i in range(1, n+1):
        if visited[i]:
            continue
        if dp[i] < min_value:
            next_index = i
            min_value = dp[i]

    if next_index != end:               # next 노드가 도착점이면 while 탈출
        stack.append(next_index)        # 아니면 스택에 푸쉬하여 다시 while 문 반복

    # print(routes)

print(dp[end])
print(len(routes[end]))
print(*routes[end])