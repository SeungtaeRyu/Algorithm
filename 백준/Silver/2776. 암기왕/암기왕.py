import sys

T = int(input())
for tc in range(1, T+1):
    _ = input()
    a = list(map(int, sys.stdin.readline().split()))
    _ = input()
    b = list(map(int, sys.stdin.readline().split()))

    a.sort()

    for num in b:
        start = 0
        end = len(a)
        mid = len(a) // 2
        while True:
            if num == a[mid]:
                print('1')
                break
            if (end - start) == 1:
                print('0')
                break
            if num > a[mid]:
                start = mid
                mid = ((end - start) // 2) + start
            else:
                end = mid
                mid = ((end - start) // 2) + start