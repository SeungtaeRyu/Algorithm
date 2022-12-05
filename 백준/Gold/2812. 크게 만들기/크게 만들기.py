import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(input().rstrip())

i = 0
count = 0
stack = []
while i != n:
    if count == k:
        stack.append(int(nums[i]))
        i += 1

    else:
        if not stack:
            stack.append(int(nums[i]))
            i += 1
            continue

        if int(nums[i]) <= stack[-1]:
            stack.append(int(nums[i]))
            i += 1
            continue
        else:
            stack.pop()
            count += 1

while count != k:
    stack.pop()
    count += 1

print("".join(list(map(str, stack))))