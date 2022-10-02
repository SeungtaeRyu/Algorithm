import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(tuple(map(float, input().split())))

edges = []
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        edges.append((i, j, ((arr[i][0]-arr[j][0])**2 + (arr[i][1]-arr[j][1])**2)**(1/2)))


edges.sort(key= lambda x: x[2])

selected = 0
e_index = 0
rep = [i for i in range(n)]
join = {i: [i] for i in range(n)}
total = 0
while selected < n-1:
    if rep[edges[e_index][0]] == rep[edges[e_index][1]]:
        e_index += 1
        continue

    if rep[edges[e_index][0]] < rep[edges[e_index][1]]:
        for edge1 in join[rep[edges[e_index][1]]]:
            rep[edge1] = rep[edges[e_index][0]]
            join[rep[edges[e_index][0]]].append(edge1)
    else:
        for edge0 in join[rep[edges[e_index][0]]]:
            rep[edge0] = rep[edges[e_index][1]]
            join[rep[edges[e_index][1]]].append(edge0)

    total += edges[e_index][2]
    selected += 1
    e_index += 1

print(f'{total:.2f}')