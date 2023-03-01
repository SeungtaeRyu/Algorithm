a, b = map(int, input().split())
c = a - a*(b/100)
if c < 100:
    print(1)
else:
    print(0)