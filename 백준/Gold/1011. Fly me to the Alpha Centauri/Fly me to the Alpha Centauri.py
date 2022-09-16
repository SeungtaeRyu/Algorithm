import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    x, y = map(int, input().split())
    d = y - x
    if d == 1:
        print(1)
    else:
        n = 1
        count = 0
        while d != 0:
            if d >= 2*n:
                count += 2
                d -= 2*n
                n += 1
            else:
                if d <= n:
                    count += 1
                    break
                else:
                    count += 2
                    break
        print(count)