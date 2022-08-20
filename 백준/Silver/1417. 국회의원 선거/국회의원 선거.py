import sys
input = sys.stdin.readline
n = int(input())
vote = [int(input()) for _ in range(n)]
count = 0
while True:
    for i in range(1, len(vote)):
        if vote[0] <= vote[i]:
            break
    else:
        break
    vote[vote.index(max(vote), 1)] -= 1
    vote[0] += 1
    count += 1
print(count)