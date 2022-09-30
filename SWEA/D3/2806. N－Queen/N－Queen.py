def f(i, k):
    global count
    for x in range(i-1):
        if p[i-1] == p[x] + (i-1-x) or p[i-1] == p[x] - (i-1-x):
            return
    if i == k:
        count += 1
    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p[i] = a[j]
                f(i+1, k)
                used[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    count = 0
    a = [i for i in range(1,N+1)]
    p = [0] * N
    used = [0] * N
    f(0, N)
    print(f'#{tc} {count}')