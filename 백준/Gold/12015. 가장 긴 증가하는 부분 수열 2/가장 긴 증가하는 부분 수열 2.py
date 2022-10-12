import sys, bisect
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

lis = []
for i in range(n):
    if not lis:
        lis.append(arr[i])
    else:
        if arr[i] > lis[-1]:
            lis.append(arr[i])
        else:
            idx = bisect.bisect_left(lis, arr[i])
            lis[idx] = arr[i]
print(len(lis))