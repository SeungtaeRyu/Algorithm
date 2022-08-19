import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())

    box = [0 for _ in range(N+1)]
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for idx in range(L, R+1):
            box[idx] = i
    print(f'#{tc} {" ".join(list(map(str, box[1:])))}')