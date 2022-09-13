visited = [False] * 10001

for i in range(1, 10001):
    n = i
    self_n = n
    while n // 10 != 0:
        self_n += n % 10
        n = n // 10
    self_n += n
    if self_n < 10001:
        visited[self_n] = True

for i in range(1, 10001):
    if visited[i] == False:
        print(i)