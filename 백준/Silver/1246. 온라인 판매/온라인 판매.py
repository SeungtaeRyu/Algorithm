n, m = map(int, input().split())

price = []
for _ in range(m):
    price.append(int(input()))
price.sort(reverse=True)

total = 0
i = 1
result = [0, 0]
while i <= n and i <= m:
    temp_total = price[i-1] * i
    if temp_total > total:
        total = temp_total
        result[0] = price[i-1]
        result[1] = price[i-1] * i
    i += 1
print(f'{result[0]} {result[1]}')