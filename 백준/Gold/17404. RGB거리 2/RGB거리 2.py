import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

Rdp = [[1000 for _ in range(3)] for _ in range(n)]
Gdp = [[1000 for _ in range(3)] for _ in range(n)]
Bdp = [[1000 for _ in range(3)] for _ in range(n)]

Rdp[0][0] = arr[0][0]
Gdp[0][1] = arr[0][1]
Bdp[0][2] = arr[0][2]

for i in range(1, n):
    Rdp[i][0] = min(Rdp[i - 1][1], Rdp[i - 1][2]) + arr[i][0]
    Rdp[i][1] = min(Rdp[i - 1][0], Rdp[i - 1][2]) + arr[i][1]
    Rdp[i][2] = min(Rdp[i - 1][0], Rdp[i - 1][1]) + arr[i][2]

    Gdp[i][0] = min(Gdp[i - 1][1], Gdp[i - 1][2]) + arr[i][0]
    Gdp[i][1] = min(Gdp[i - 1][0], Gdp[i - 1][2]) + arr[i][1]
    Gdp[i][2] = min(Gdp[i - 1][0], Gdp[i - 1][1]) + arr[i][2]

    Bdp[i][0] = min(Bdp[i - 1][1], Bdp[i - 1][2]) + arr[i][0]
    Bdp[i][1] = min(Bdp[i - 1][0], Bdp[i - 1][2]) + arr[i][1]
    Bdp[i][2] = min(Bdp[i - 1][0], Bdp[i - 1][1]) + arr[i][2]


print(min(Rdp[n-1][1], Rdp[n-1][2], Gdp[n-1][0], Gdp[n-1][2], Bdp[n-1][0], Bdp[n-1][1]))