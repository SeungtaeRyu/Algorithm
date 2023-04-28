sold = dict()
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    if a not in sold:
        sold[a] = [b]
    else:
        sold[a].append(b)
result = 0
top = 0
for i in sorted(list(sold.keys())):
    t = 0
    for j in sold:
        for z in sold[j]:
            if i-z > 0:
                t += i-z
    del sold[i]
    if top < t:
        top = t
        result = i

print(result)