import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
start, end = 0, 0
count = 1 if nums[0] == 1 else 0
minV = n+1
while start != n:
    if count == k:
        minV = min(minV, end-start+1)

    if count < k:
        if end < len(nums) -1:
            end += 1
            if nums[end] == 1:
                count += 1
        else:
            break

    elif count >= k:
        if nums[start] == 1:
            count -= 1
        start += 1

if minV == n+1:
    print(-1)
else:
    print(minV)