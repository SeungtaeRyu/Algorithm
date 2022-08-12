N, M = map(int, input().split())

ase = list(range(1, N+1))
yp = []

index = M-1
for i in range(1, N+1):

    yp.append(ase[index])
    if i == N:
        break
    ase.pop(index)
    index = (index+M-1) % (N-i)

print('<' + ', '.join(list(map(str, yp))) + '>')