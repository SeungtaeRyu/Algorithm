import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    arr = list(input())

    total = 0
    bar = 0
    flag = False
    for i in range(len(arr)):
        if arr[i] == '(':           # 나무 or 레이저? 일단 나무 한개 올리고, 레이저 준비
            bar += 1
            flag = True
        elif flag:                  # 레이저 일 때, 일단 올렸던 나무 다시 빼고, 현재 나무막대기 갯수만큼 total 에 증가
            bar -= 1
            total += bar
            flag = False
        else:                       # 막대기가 닫힐때, 현재 막대기 갯수 -1, total +1
            bar -= 1
            total += 1
    print(f'#{tc} {total}')