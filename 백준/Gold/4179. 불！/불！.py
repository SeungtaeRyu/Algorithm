import sys
input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]

f_stack = []
j_stack = []
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'F':
            f_stack.append((i, j))
        elif arr[i][j] == 'J':
            j_stack.append((i, j))

if j_stack[0][0] == 0 or j_stack[0][0] == r-1 or j_stack[0][1] == 0 or j_stack[0][1] == c-1:
    print(1)
    exit()

flag = False
count = 0
while True:
    f_stack2 = []
    while f_stack:
        cx, cy = f_stack.pop()
        if cx-1 >= 0:
            if arr[cx-1][cy] == '.' or arr[cx-1][cy] == 'J':
                arr[cx-1][cy] = 'F'
                f_stack2.append((cx-1, cy))
        if cy-1 >= 0:
            if arr[cx][cy-1] == '.' or arr[cx][cy-1] == 'J':
                arr[cx][cy-1] = 'F'
                f_stack2.append((cx, cy-1))
        if cx+1 < r:
            if arr[cx+1][cy] == '.' or arr[cx+1][cy] == 'J':
                arr[cx+1][cy] = 'F'
                f_stack2.append((cx+1, cy))
        if cy+1 < c:
            if arr[cx][cy+1] == '.' or arr[cx][cy+1] == 'J':
                arr[cx][cy+1] = 'F'
                f_stack2.append((cx, cy+1))

    j_stack2 = []
    while j_stack:
        cx, cy = j_stack.pop()
        if cx-1 >= 0:
            if arr[cx-1][cy] == '.':
                arr[cx-1][cy] = 'J'
                j_stack2.append((cx-1, cy))
                if cx-1 == 0:
                    flag = True
                    break
        if cy-1 >= 0:
            if arr[cx][cy-1] == '.':
                arr[cx][cy-1] = 'J'
                j_stack2.append((cx, cy-1))
                if cy-1 == 0:
                    flag = True
                    break
        if cx+1 < r:
            if arr[cx+1][cy] == '.':
                arr[cx+1][cy] = 'J'
                j_stack2.append((cx+1, cy))
                if cx+1 == r-1:
                    flag = True
                    break
        if cy+1 < c:
            if arr[cx][cy+1] == '.':
                arr[cx][cy+1] = 'J'
                j_stack2.append((cx, cy+1))
                if cy+1 == c-1:
                    flag = True
                    break

    f_stack = f_stack2[:]
    j_stack = j_stack2[:]
    count += 1

    if flag:
        break
    else:
        if not j_stack:
            print("IMPOSSIBLE")
            exit()

print(count+1)