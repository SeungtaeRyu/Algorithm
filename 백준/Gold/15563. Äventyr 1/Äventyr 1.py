import sys
input = sys.stdin.readline

n, q = map(int, input().split())
input()
nums = [False for _ in range(100001)]
num_count = 0
minV = 100001
maxV = 0
for i in range(q):
    c, v = map(int, input().split())
    if c == 1:
        nums[v] = True
        num_count += 1
        minV = min(minV, v)
        maxV = max(maxV, v)
    else:
        if num_count == 0:
            print(-1)
        else:
            if v <= minV:
                print(minV - v)
            elif v >= maxV:
                print(v - maxV)
            else:
                count = 0
                while True:
                    if nums[v-count] or nums[v+count]:
                        break
                    count += 1
                print(count)