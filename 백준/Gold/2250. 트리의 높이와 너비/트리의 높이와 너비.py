import sys
input = sys.stdin.readline

def inorder(node):
    global level, count
    if tree[node][0] != -1:
        level += 1
        inorder(tree[node][0])
    node_level[count] = level
    count += 1
    if tree[node][1] != -1:
        level += 1
        inorder(tree[node][1])
    level -= 1

n = int(input())
tree = {i: [] for i in range(1, n+1)}
node_level = [0] * (n+1)
isparents = [False] * (n+1)

for _ in range(n):
    node, left, right = map(int, input().split())
    tree[node].append(left)
    tree[node].append(right)
    if left != -1:
        isparents[left] = True
    if right != -1:
        isparents[right] = True

for i in range(1, n + 1):
    if isparents[i] == False:
        root = i

level = 1
count = 1
inorder(root)

max_width = 0
ans_level = 1
level = 1
while node_level.count(level) != 0:
    same_level_list = list(filter(lambda x: node_level[x] == level, range(len(node_level))))
    if max(same_level_list) - min(same_level_list) > max_width:
        max_width = max(same_level_list) - min(same_level_list)
        ans_level = level
    level += 1

print(f'{ans_level} {max_width+1}')