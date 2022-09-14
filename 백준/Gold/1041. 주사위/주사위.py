import sys
input = sys.stdin.readline

n = int(input())
dice = list(map(int, input().split()))

across = {
    0: 5,
    1: 4,
    2: 3,
    3: 2,
    4: 1,
    5: 0
}

sorted_dice = sorted(dice)

# 1개 면 최소값 min_1 에 저장
min_1 = sorted_dice[0]

# 2개 면 최소값 min_2 에 저장
if dice[across[dice.index(sorted_dice[0])]] == sorted_dice[1]:
    min_2 = sorted_dice[0] + sorted_dice[2]
else:
    min_2 = sorted_dice[0] + sorted_dice[1]

# 3개 면 최소값 min_3 에 저장
min_3 = sys.maxsize
for i in range(2, 4):
    min_3 = min(min_3, dice[i] + dice[0] + dice[1])
    min_3 = min(min_3, dice[i] + dice[1] + dice[5])
    min_3 = min(min_3, dice[i] + dice[5] + dice[4])
    min_3 = min(min_3, dice[i] + dice[4] + dice[0])

# 3면 쓰는 곳 개수
count_3 = 4
# 2면 쓰는 곳 개수
count_2 = 4*(n-1) + 4*(n-2)
# 1면 쓰는 곳 개수
count_1 = 0
for i in range(2, n):
    count_1 += 2*(i-1)
count_1 = count_1 * 4 + (n-2)**2

if n == 1:
    print(sum(sorted_dice[:5]))
else:
    print(min_1*count_1 + min_2*count_2 + min_3*count_3)