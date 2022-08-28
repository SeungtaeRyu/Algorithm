import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    isreverse = False
    p = list(input().strip())
    n = int(input())
    x = input().rstrip()[1:-1].split(",")
    if n == 0:
        x = []
    for i in p:
        if i == 'R':
            isreverse = not isreverse
        else:
            if x:
                if isreverse:
                    x.pop()
                else:
                    x.pop(0)
            else:
                print('error')
                break
    else:
        if isreverse:
            print("[" + ','.join(x[::-1]) + "]")
        else:
            print("[" + ','.join(x) + "]")