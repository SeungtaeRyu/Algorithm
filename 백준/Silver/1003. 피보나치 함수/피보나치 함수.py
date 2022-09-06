import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    dp_count0 = [0] * 41
    dp_count1 = [0] * 41

    dp_count0[0] = 1
    dp_count1[1] = 1
    for i in range(2, n+1):
        dp_count0[i] = dp_count0[i-1]+dp_count0[i-2]
        dp_count1[i] = dp_count1[i-1]+dp_count1[i-2]
    print(dp_count0[n], dp_count1[n])