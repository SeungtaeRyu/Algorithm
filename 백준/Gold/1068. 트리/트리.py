import sys
input = sys.stdin.readline
n = int(input())
tree = {i: [] for i in range(n)}
info = list(map(int, input().split()))
delete_node = int(input())
for i in range(n):
    if info[i] == -1:
        root = i
        continue
    if i == delete_node:
        continue
    tree[info[i]].append(i)
if root == delete_node:
    print(0)
else:
    stack = [root]
    ans = 0
    while stack:
        now_node = stack.pop()
        if len(tree[now_node]) == 0:
            ans += 1
        for next_node in tree[now_node]:
            stack.append(next_node)
    print(ans)