import sys
input = sys.stdin.readline


n = int(input())
ships = list(map(int, input().split()))
m = int(input())
weight = list(map(int, input().split()))

ships.sort(reverse=True)
weight.sort(reverse=True)

if ships[0] < weight[0]:
    print(-1)
else:
    count = 0
    while weight:
        count += 1
        for ship in ships:
            index = 0
            while index < len(weight):
                if ship >= weight[index]:
                    weight.pop(index)
                    break
                else:
                    index += 1
    print(count)
