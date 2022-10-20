import sys
input = sys.stdin.readline

def f(arr, k):
    value = arr[0][0]
    flag = False
    for i in range(k):
        for j in range(k):
            if arr[i][j] != value:
                flag = True
                break
        if flag:
            break

    if flag:
        if k == 3:
            for i in range(k):
                for j in range(k):
                    cnt[arr[i][j]] += 1

        else:
            for i in range(0, k, k // 3):
                for j in range(0, k, k // 3):
                    n_arr = []
                    for x in range(k // 3):
                        n_arr.append(arr[i+x][j:j+k//3])
                    f(n_arr, k//3)

                    # n_arr = [arr[i][j:j+k//3], arr[i+1][j:j+k//3], arr[i+2][j:j+k//3]]

    else:
        cnt[value] += 1
        pass
    pass

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


cnt = [0, 0, 0]

if n == 1:
    cnt[arr[0][0]] += 1
    print(cnt[-1])
    print(cnt[0])
    print(cnt[1])

else:
    f(arr, n)
    print(cnt[-1])
    print(cnt[0])
    print(cnt[1])