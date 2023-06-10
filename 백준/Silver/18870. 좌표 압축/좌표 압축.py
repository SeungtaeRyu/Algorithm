import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
set_nums = set(nums)
sorted_nums = sorted(set_nums)

for num in nums:

    start, end = 0, len(sorted_nums) - 1
    while start != end:
        mid = (start + end) // 2
        if sorted_nums[mid] > num:
            end = mid - 1
        elif sorted_nums[mid] < num:
            start = mid + 1
        else:
            end -= 1
    print(start, end=" ")