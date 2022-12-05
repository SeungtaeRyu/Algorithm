import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

digree = [0 for _ in range(k+1)]

for num in nums:
    digree[num] += 1

count = 0
stack = []
for i in range(k):
    if nums[i] in stack:
        continue

    if len(stack) != n:
        stack.append(nums[i])
        digree[nums[i]] -= 1
    else:
        temp = [sys.maxsize for _ in range(len(stack))]
        for j in range(len(stack)):
            for l in range(i+1, k):
                if nums[l] == stack[j]:
                    temp[j] = l
                    break
        stack.pop(temp.index(max(temp)))

        stack.append(nums[i])
        count += 1

print(count)