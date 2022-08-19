import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    count_arr = [[] for _ in range(n)]
    count = 0

    # N 극은 1
    # S 극은 2
    for i in range(n):
        for j in range(n):
            # 첫 입력을 검증할 if 문
            if len(count_arr[i]) == 0:
                if arr[j][i] == 1:
                    count_arr[i].append(arr[j][i])
                else:
                    continue
            # 첫 입력 이후는 이전 입력이 1일때 2, 이전 입력이 2일때 1이 들어올때만 append
            elif arr[j][i] != 0 and arr[j][i] != count_arr[i][-1]:
                count_arr[i].append(arr[j][i])
        count += len(count_arr[i]) // 2

    print(f'#{tc} {count}')