import sys, heapq
input = sys.stdin.readline

n, m = map(int ,input().split())

info = []
# for _ in range(m):
#     info.append(tuple(map(int, input().split())))
# info.sort(key=lambda x: x[2])
for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(info, (c, a, b))
# print(info)

adj = {i: [i] for i in range(1, n+1)}
rep = [i for i in range(n+1)]

edge_count = 0
# index = 0
total = 0
while edge_count < n-2:
    c, a, b = heapq.heappop(info)
    # print(info[index])
    # a, b, c = info[index]

    if rep[a] == rep[b]:
        # index += 1
        continue
    # print(a,b,c)
    # print(rep)
    if rep[a] < rep[b]:
        y = rep[b]
        # print(y)
        while adj[y]:
            x = adj[y].pop()
            rep[x] = rep[a]
            adj[rep[a]].append(x)

        # for x in adj[rep[b]]:
        #     rep[x] = rep[a]
        #     adj[a].append(x)
    else:
        y = rep[a]
        while adj[y]:
            x = adj[y].pop()
            rep[x] = rep[b]
            adj[rep[b]].append(x)

        # for x in adj[rep[a]]:
        #     rep[x] = rep[b]
        #     adj[b].append(x)

    total += c
    # index += 1
    edge_count += 1
# print()

print(total)

# print(adj)
# print(rep)

# adj = {i: [] for i in range(1, n+1)}
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     adj[a].append((b, c))
#     adj[b].append((a, c))
#
# print(adj)

