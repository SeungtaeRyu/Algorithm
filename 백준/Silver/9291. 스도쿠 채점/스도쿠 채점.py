import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    flag = "CORRECT"

    for i in range(9):
        temp = set()
        temp2 = set()
        for j in range(9):
            temp.add(arr[i][j])
            temp2.add(arr[j][i])
        if len(temp) != 9 or len(temp2) != 9:
            flag = "INCORRECT"
            break

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            temp = set()
            for k in range(3):
                for l in range(3):
                    temp.add(arr[i+k][j+l])
            if len(temp) != 9:
                flag = "INCORRECT"
                break

    print(f'Case {tc}: {flag}')
    if tc != T:
        input()
