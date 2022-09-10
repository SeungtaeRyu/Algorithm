import sys
input = sys.stdin.readline

rope = []
for _ in range(int(input())):
    rope.append(int(input()))

rope.sort(reverse=True)

maxValue = rope[0]
for i in range(len(rope)):
    if maxValue < rope[i] * (i+1):
        maxValue = rope[i] * (i+1)
print(maxValue)