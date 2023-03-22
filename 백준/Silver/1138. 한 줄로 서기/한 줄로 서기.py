import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
answer = [0 for i in range(n)]

cur = nums[0]
answer[cur] = 1
for i in range(1, len(nums)):
    x = nums[i-1] - nums[i]
    if x > 0:
        count = 1
        _next = cur - 1
        while True:
            if answer[_next] == 0:
                if count == x:
                    answer[_next] = i+1
                    cur = _next
                    break
                else:
                    count += 1
                    _next -= 1
            else:
                _next -= 1
    else:
        count = 0
        _next = cur + 1
        while True:
            if answer[_next] == 0:
                if count == x:
                    answer[_next] = i+1
                    cur = _next
                    break
                else:
                    count -= 1
                    _next += 1
            else:
                _next += 1
print(*answer)

