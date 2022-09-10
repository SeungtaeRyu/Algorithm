import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

adj = {i: [] for i in range(n+1)}
for _ in range(m):
    x, y, p = map(int, input().split())
    adj[x].append((y, p))

dp = [1e9] * (n+1)
visited = [False] * (n+1)

start, end = map(int, input().split())

stack = [start]
dp[start] = 0
while stack:
    now_node = stack.pop()
    visited[now_node] = True
    for next_node, next_price in adj[now_node]:
        if visited[next_node]:
            continue
        else:
            dp[next_node] = min(dp[now_node] + next_price, dp[next_node])

    min_node_index = -1
    for i in range(1, n+1):
        if visited[i]:
            continue
        if min_node_index == -1:
            min_node_index = i
        else:
            if dp[min_node_index] > dp[i]:
                min_node_index = i
    if min_node_index != end:
        stack.append(min_node_index)

print(dp[end])