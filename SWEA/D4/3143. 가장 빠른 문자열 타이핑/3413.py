import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()                      # A = 'hellolll', B = 'll'
    print(f"#{tc} {len(A.replace(B,' '))}")     # len('he o l') => 6
