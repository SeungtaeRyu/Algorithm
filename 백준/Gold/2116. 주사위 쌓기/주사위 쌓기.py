import sys
input = sys.stdin.readline

dice = []
for _ in range(int(input())):
    dice.append(list(map(int, input().split())))
# print(dice)
# 인덱스 0 - 5 // 1 - 3 // 2 - 4
result = 0
for i in range(6):
    # total = 0
    # top_number = dice[0][i]
    # bottom_number =
    #
    # count = 1
    # print(dice[0][i])
    # print(f'total = {total}')
    top_number = dice[0][i]
    count = 0
    total = 0
    while count < len(dice):
        bottom_number = top_number
        bottom_index = dice[count].index(top_number)
        if bottom_index == 0:
            top_index = 5
        if bottom_index == 1:
            top_index = 3
        if bottom_index == 2:
            top_index = 4
        if bottom_index == 3:
            top_index = 1
        if bottom_index == 4:
            top_index = 2
        if bottom_index == 5:
            top_index = 0
        top_number = dice[count][top_index]
        # print(f'bottom_number = {bottom_number}')
        # print(f'top_number = {top_number}')

        if top_number == 6:
            if bottom_number == 5:
                total += 4
            else:
                total += 5
        elif top_number == 5:
            if bottom_number == 6:
                total += 4
            else:
                total += 6
        else:
            if bottom_number == 6:
                total += 5
            else:
                total += 6
        count += 1
        # print(f'total = {total}')
    result = max(result, total)
print(result)