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
        if k == 2:
            for i in range(k):
                for j in range(k):
                    cnt[arr[i][j]] += 1

        else:
            for i in range(0, k, k // 2):
                for j in range(0, k, k // 2):
                    n_arr = []
                    for x in range(k // 2):
                        n_arr.append(arr[i+x][j:j+k//2])
                    f(n_arr, k//2)

    else:
        cnt[value] += 1


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


cnt = [0, 0]


f(arr, n)
print(cnt[0])
print(cnt[1])