import sys
input = sys.stdin.readline

score=[]
for i in range(int(input())):
    score.append(float(input()))
score.sort()
for i in range(7):
    print(f'{score[i]:0.3f}')