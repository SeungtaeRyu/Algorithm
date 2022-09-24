import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    tree = {i: 0 for i in range(1, n+1)}

    for i in range(n-1):
        p, c = map(int, input().split())
        tree[c] = p

    a, b = map(int, input().split())

    a_parents = [a]
    b_parents = [b]

    while tree[a] != 0:
        a_parents.append(tree[a])
        a = tree[a]
    while tree[b]:
        b_parents.append(tree[b])
        b = tree[b]

    index = -1
    while True:
        if abs(index) > len(a_parents) or abs(index) > len(b_parents):
            print(a_parents[index+1])
            break
        if a_parents[index] == b_parents[index]:
            index -= 1
        else:
            print(a_parents[index+1])
            break