import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

start = 0
end = n-1

ans_start = 0
ans_end = 0

hap = sys.maxsize
while start != end:
    if abs(nums[start] + nums[end]) <= hap:
        hap = abs(nums[start] + nums[end])
        ans_start = start
        ans_end = end

    if nums[start] + nums[end] > 0:
        end -= 1
    elif nums[start] + nums[end] < 0:
        start += 1
    else:
        ans_start = start
        ans_end = end
        break
print(f'{nums[ans_start]} {nums[ans_end]}')