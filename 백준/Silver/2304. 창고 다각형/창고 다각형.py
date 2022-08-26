import sys
input = sys.stdin.readline

bar = []
for i in range(int(input())):
    bar.append(tuple(map(int, input().split())))


max_bar = max(bar, key=lambda x:x[1])

bar.sort()

cur_x = bar[0][0]
cur_y = bar[0][1]
area = max_bar[1]
for i in range(len(bar)):
    next_x = bar[i][0]
    next_y = bar[i][1]
    if next_x == max_bar[0]:
        area = area + (next_x - cur_x) * cur_y
        break
    elif cur_y < next_y:
        area = area + (next_x - cur_x) * cur_y
        cur_x = next_x
        cur_y = next_y

cur_x = bar[-1][0]
cur_y = bar[-1][1]
for i in range(len(bar)-1, -1, -1):
    next_x = bar[i][0]
    next_y = bar[i][1]
    if next_x == max_bar[0]:
        area = area + (cur_x - next_x) * cur_y
        break
    elif cur_y < next_y:
        area = area + (cur_x - next_x) * cur_y
        cur_x = next_x
        cur_y = next_y

print(area)
