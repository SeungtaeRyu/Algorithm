import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

start = 0
end = 0

total = nums[0]
min_length = 100001
while start < len(nums):
    if total < s:
        if end == len(nums)-1:
            break
        end += 1
        total += nums[end]
    elif total >= s:
        min_length = min(min_length, end-start+1)
        total -= nums[start]
        start += 1

if min_length == 100001:
    print(0)
else:
    print(min_length)