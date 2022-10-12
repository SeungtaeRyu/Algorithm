import sys, bisect
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

arr = []

# a의 값을 가지는 b의 인덱스 배열 구하기
new_a = dict()
new_b = dict()
for i in range(n):
    new_a[i+1] = a[i]
    new_b[b[i]] = i+1

# print(new_a)
# print(new_b)

for i in range(1, n+1):
    arr.append(new_b[new_a[i]])

# print(arr)

# lis를 구한다 - O(NlogN)
lis = []
for i in range(n):
    if not lis:
        lis.append(arr[i])
    else:
        if arr[i] > lis[-1]:
            lis.append(arr[i])
        else:
            # idx : lower_bound의 인덱스
            idx = bisect.bisect_left(lis, arr[i])
            lis[idx] = arr[i]
print(len(lis))
# arr = list(map(int, sys.stdin.readline().split()))
# inc_arr = [sys.maxsize]*n
#
# for i in range(0,n):
#     idx = bisect.bisect_left(inc_arr, arr[i])
#     inc_arr[idx] = arr[i]
# print(bisect.bisect_left(inc_arr, sys.maxsize))
# dp = [new_b[0]]
#
# for i in range(n):
#     if new_b[i] > dp[-1]:
#         dp.append(new_b[i])
#     else:
#         idx = bisect.bisect_left(dp, new_b[i])
#         dp[idx] = new_b[i]
#
# print(len(dp))
#
# print(dp)

# print(new_b)

# LIS = [0] * (n)
# LIS[0] = 1
# for i in range(1, n):
#     for j in range(i-1, -1, -1):
#         if new_b[i] > new_b[j]:
#             LIS[i] = max(LIS[i], LIS[j]+1)
#         if LIS[i] == max(LIS):
#             break
#
# print(LIS[n-1])


# import sys, bisect
#
# # 입력부
# n = int(sys.stdin.readline())
# a = list(map(int, sys.stdin.readline().split()))
# b = list(map(int, sys.stdin.readline().split()))
#
# # da : 현재 a의 원소의 값을 key, 그 때의 인덱스를 value로 갖는 딕셔너리
# da = dict().fromkeys([i for i in range(n + 1)], -1)
# # da : 현재 b의 원소의 값을 key, 그 때의 인덱스를 value로 갖는 딕셔너리
# db = dict().fromkeys([i for i in range(n + 1)], -1)
#
# for i in range(n):
#     da[a[i]] = i
#     db[b[i]] = i
#
# # arr : A를 기준으로 하는 B배열의 인덱스 배열. 그림 3의 오른쪽 위 배열 그림과 같다
# arr = []
# for i in range(n):
#     arr.append(db[a[i]])
#
# print(arr)
#
# # lis를 구한다 - O(NlogN)
# lis = []
# for i in range(n):
#     if not lis:
#         lis.append(arr[i])
#     else:
#         if arr[i] > lis[-1]:
#             lis.append(arr[i])
#         else:
#             # idx : lower_bound의 인덱스
#             idx = bisect.bisect_left(lis, arr[i])
#             lis[idx] = arr[i]
#
# # 정답 출력
# print(len(lis))


# 10
# 1 7 3 2 5 10 4 6 8 9
# 1 2 3 4 5 10 9 8 7 6