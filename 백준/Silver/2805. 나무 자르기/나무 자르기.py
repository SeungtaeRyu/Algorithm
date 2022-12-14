import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)
while start != end:
    mid = (start + end) // 2

    count = 0
    for tree in trees:
        if tree > mid:
            count += (tree - mid)

    if count >= m:
        start = mid + 1
    else:
        end = mid

print(start-1)