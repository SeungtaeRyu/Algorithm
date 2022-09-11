import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

adj = {i: [] for i in range(n+1)}
routes = {i: [] for i in range(n+1)}                # routes 딕셔너리 선언
for _ in range(m):
    x, y, p = map(int, input().split())
    adj[x].append((y, p))

dp = [sys.maxsize] * (n+1)
visited = [False] * (n+1)

start, end = map(int, input().split())

stack = [start]
dp[start] = 0
routes[start] = [start]                        # start route 추가
while stack:
    now_node = stack.pop()
    visited[now_node] = True
    for next_node, next_price in adj[now_node]:
        if visited[next_node]:
            continue
        else:
            if dp[now_node] + next_price < dp[next_node]:               # dp[i]가 갱신 될 때마다
                dp[next_node] = dp[now_node] + next_price
                routes[next_node] = routes[now_node] + [next_node]      # route[i]도 같이 갱신

    next_index = 0
    min_value = sys.maxsize
    for i in range(1, n+1):
        if visited[i]:
            continue
        if dp[i] < min_value:
            next_index = i
            min_value = dp[i]

    if next_index != end:
        stack.append(next_index)

print(dp[end])
print(len(routes[end]))             # 루트 길이 출력
print(*routes[end])                 # 루트 경로 출력