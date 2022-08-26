cham = int(input())

byun_x = []
byun_y = []
byun_list = []
for i in range(6):
    vector, value = map(int, input().split())
    byun_list.append((vector, value))
    if i % 2:
        byun_x.append(value)
    else:
        byun_y.append(value)

for i in range(6):
    if byun_list[i][0] == byun_list[i-2][0] and byun_list[i-1][0] == byun_list[i-3][0]:
        x = i


big_area = max(byun_x) * max(byun_y)
small_area = byun_list[x-1][1] * byun_list[x-2][1]

print((big_area-small_area) * cham)
