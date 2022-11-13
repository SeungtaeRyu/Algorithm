import sys
input = sys.stdin.readline

n = int(input())
point = dict()
for i in range(n):
    x, y = map(int, input().split())
    if point.get(x) == None:
        point[x] = [y]
    else:
        point[x].append(y)

point = sorted(point.items())

value = [0, 0]

if len(point) == 1:
    print(0)
else:
    for i in range(len(point)-1):
        x1 = point[i][0]
        maxy1 = max(point[i][1])
        miny1 = min(point[i][1])

        x2 = point[i+1][0]
        maxy2 = max(point[i+1][1])
        miny2 = min(point[i+1][1])

        max_max = value[0] + ((x2-x1)**2 + (maxy2-maxy1)**2)**(0.5)
        max_min = value[0] + ((x2-x1)**2 + (miny2-maxy1)**2)**(0.5)
        min_max = value[1] + ((x2-x1)**2 + (maxy2-miny1)**2)**(0.5)
        min_min = value[1] + ((x2-x1)**2 + (miny2-miny1)**2)**(0.5)

        value[0] = max(min_max, max_max)
        value[1] = max(min_min, max_min)

    print(f'{max(value):.7f}')
