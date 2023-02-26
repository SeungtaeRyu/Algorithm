import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [True for _ in range(m + 1)]
nums[1] = False

for i in range(2, m+1):
    if nums[i]:
        if i >= n:
            print(i)
        j = i+i
        while j < m+1:
            nums[j] = False
            j+=i