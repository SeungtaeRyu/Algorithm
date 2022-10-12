import sys, bisect
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

arr = []

new_a = dict()
new_b = dict()
for i in range(n):
    new_a[i+1] = a[i]
    new_b[b[i]] = i+1

for i in range(1, n+1):
    arr.append(new_b[new_a[i]])

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