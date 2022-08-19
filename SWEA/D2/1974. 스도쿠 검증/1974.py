import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):

    arr = [list(map(int, input().split())) for _ in range(9)]
    n_arr = list(zip(*arr))
    n_n_arr = []
    for i in range(3):
        for j in range(3):
            n_n_arr.append(arr[3*i][3*j:3*j+3] + arr[3*i+1][3*j:3*j+3] + arr[3*i+2][3*j:3*j+3])

    for i in range(9):
        if len(set(arr[i])) == 9 and len(set(n_arr[i])) == 9 and len(set(n_n_arr[i])) == 9:
            continue
        else:
            break
    else:
        print(f'#{tc} 1')
        continue
    print(f'#{tc} 0')
