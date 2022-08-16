import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    result = ''
    # 가로 검증
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M//2):
                if arr[i][j+k] != arr[i][M-1+j-k]:
                    break
            else:
                result = ''.join(arr[i][j:j+M])

    # 세로 검증
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M//2):
                if arr[j+k][i] != arr[M-1+j-k][i]:
                    break
            else:
                for l in range(M):
                    result += arr[j+l][i]

    print(f'#{tc} {result}')