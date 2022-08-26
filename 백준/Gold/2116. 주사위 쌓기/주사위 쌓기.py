import sys
input = sys.stdin.readline

dice = []
for _ in range(int(input())):
    dice.append(list(map(int, input().split())))
result = 0
for i in range(6):

    top_number = dice[0][i]
    count = 0
    total = 0
    while count < len(dice):
        bottom_number = top_number
        bottom_index = dice[count].index(top_number)
        
        if bottom_index == 0:
            top_index = 5
        elif bottom_index == 1:
            top_index = 3
        elif bottom_index == 2:
            top_index = 4
        elif bottom_index == 3:
            top_index = 1
        elif bottom_index == 4:
            top_index = 2
        else:
            top_index = 0
            
        top_number = dice[count][top_index]
        for num in range(6,0,-1):
            if num != top_number and num != bottom_number:
                total += num
                break

        count += 1
    result = max(result, total)
print(result)