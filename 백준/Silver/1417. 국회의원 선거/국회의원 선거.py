import sys
input = sys.stdin.readline

n = int(input())                                # 4                     3
vote = [int(input()) for _ in range(n)]         # [10, 10, 10, 10]      [5, 7, 7]

count = 0
while True:
    for i in range(1, len(vote)):
        if vote[0] <= vote[i]:
            break
    else:
        break
    # print(vote.index(max(vote[1:]),1))
    vote[vote.index(max(vote[1:]), 1)] -= 1
    vote[0] += 1
    count += 1
print(count)