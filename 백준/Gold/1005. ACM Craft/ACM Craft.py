import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))

    indegree = [0] * (n+1)
    rule = {i: [] for i in range(1, n+1)}
    for _ in range(k):
        value, key = map(int, input().split())
        rule[value].append(key)
        indegree[key] += 1

    target = int(input())

    dp = [0] * (n+1)

    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i]

    while q:
        now = q.popleft()
        for i in rule[now]:
            dp[i] = max(dp[i], dp[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    print(dp[target])