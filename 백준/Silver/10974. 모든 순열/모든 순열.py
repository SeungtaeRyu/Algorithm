
def f(i, k):
    if i == k:
        print(*p)
    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p[i] = a[j]
                f(i+1, k)
                used[j] = 0

n = int(input())
a = [i for i in range(1, n+1)]
used = [0 for i in range(n)]
p = [0 for i in range(n)]

f(0, n)