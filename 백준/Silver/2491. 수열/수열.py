import sys
input = sys.stdin.readline

_ = input()
max_count = 1
min_count = 1
ans = 1
numbers = list(map(int, input().split()))
for i in range(1, len(numbers)):
    if numbers[i] >= numbers[i-1]:
        max_count += 1
    else:
        ans = max(ans, max_count, min_count)
        max_count = 1
    if numbers[i] <= numbers[i-1]:
        min_count += 1
    else:
        ans = max(ans, max_count, min_count)
        min_count = 1
print(max(ans, max_count, min_count))