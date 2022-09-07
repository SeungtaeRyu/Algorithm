a, b, v = map(int, input().split())

x = v - a
y = a - b
if x % y == 0:
    c = x//y
else:
    c = x//y + 1

print(c+1)