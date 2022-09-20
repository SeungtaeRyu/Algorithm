n = int(input())

count = 0
if n % 2:
    n -= 5
    count += 1

if n < 0:
    print(-1)
elif n >= 10:
    count += (n // 10) * 2
    n %= 10
    count += n // 2
    print(count)
else:
    count += n // 2
    print(count)
