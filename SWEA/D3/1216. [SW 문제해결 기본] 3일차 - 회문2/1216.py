import sys
sys.stdin = open("input.txt")

for _ in range(1, 11):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    count = 1
    # 가로 검증
    for i in range(100):
        for j in range(100):
            for k in range(j + 1, 100):
                for l in range(k - j + 1 // 2):
                    if arr[i][j + l] != arr[i][k - l]:
                        break
                else:
                    count = max(count, k - j + 1)

    # 세로 검증
    for i in range(100):
        for j in range(100):
            for k in range(j + 1, 100):
                for l in range(k - j + 1 // 2):
                    if arr[j + l][i] != arr[k - l][i]:
                        break
                else:
                    count = max(count, k - j + 1)
    # 정답 출력
    print(f'#{tc} {count}')