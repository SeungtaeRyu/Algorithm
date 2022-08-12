n, m = map(int, input().split())

S = set()

for _ in range(n):
    S.add(input())

count = 0

for _ in range(m):
    word = set()
    word.add(input())
    if word & S == word:
        count += 1
print(count)