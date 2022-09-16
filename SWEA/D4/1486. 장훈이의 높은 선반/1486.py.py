def f(i, n, t, b):
    global min_top
    if t >= b:
        min_top = min(t, min_top)
    if i == n:
        return
    else:
        f(i+1, n, t + numbers[i], b)
        f(i+1, n, t, b)

T = int(input())
for tc in range(1, T+1):
    n, b = map(int, input().split())
    numbers = list(map(int, input().split()))

    min_top = sum(numbers)
    f(0, n, 0, b)
    print(f'#{tc} {min_top-b}')