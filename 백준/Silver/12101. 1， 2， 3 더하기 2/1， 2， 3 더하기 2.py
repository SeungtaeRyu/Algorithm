import sys
input = sys.stdin.readline

def f(total, list1):
    global count, ans
    if total > n:
        return

    if total == n:
        count += 1

        if count == k:
            ans = list1[:]

    else:
        for i in range(1, 4):
            list1.append(i)
            f(total + i, list1)
            list1.pop()

n, k = map(int, input().split())

count = 0
ans = []
f(0, [])

if not ans:
    print(-1)
else:
    print('+'.join(map(str, ans)))