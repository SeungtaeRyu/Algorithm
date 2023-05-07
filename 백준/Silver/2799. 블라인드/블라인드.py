a, b = map(int, input().split())

info = list()
for _ in range(5 * a + 1):
    info.append(input())

test = str()
for j in range(1, 5 * b + 1, 5):
    for i in range(5 * a + 1):
        test += info[i][j:j + 4]

test = test.split('####')

target = {'................': 0
, '****............': 0
, '********........': 0
, '************....': 0
, '****************': 0}

for i in test:
    if i in target:
        target[i] += 1

for item in target:
    print(target[item], end=' ')