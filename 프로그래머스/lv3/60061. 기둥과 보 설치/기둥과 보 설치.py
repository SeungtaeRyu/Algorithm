
def bo_can(x,y,arr,bo,gi,n):
    # 왼쪽끝이 기둥
    if y > 0 and arr[x][y - 1][gi]:
        return True
    # 오른쪽끝이 기둥
    elif y > 0 and x < n - 1 and arr[x + 1][y - 1][gi]:
        return True
    # 양쪽끝이 보
    elif x > 0 and x < n - 1 and arr[x - 1][y][bo] and arr[x + 1][y][bo]:
        return True
    return False

def gi_can(x,y,arr,bo,gi,n):
    # 바닥
    if y == 0:
        return True
    # 보의 한쪽 끝
    elif x > 0 and arr[x - 1][y][bo]:
        return True
    elif arr[x][y][bo]:
        return True
    # 다른 기둥 위
    elif y > 0 and arr[x][y - 1][gi]:
        return True
    return False

def solution(n, build_frame):
    answer = []
    n = n + 1
    arr = [[[0, 0] for i in range(n)] for i in range(n)]

    gi = 0
    bo = 1

    # build_frame = 가로좌표, 세로좌표, 기둥or보(0,1), 삭제or설치 (0,1)
    for x ,y ,a ,b in build_frame:
        if b:
            # 보 설치기준
            if a:
                if bo_can(x,y,arr,bo,gi,n):
                    arr[x][y][bo] = 1
            # 기둥 설치기준
            else:
                if gi_can(x,y,arr,bo,gi,n):
                    arr[x][y][gi] = 1

        # 삭제
        else:

            arr[x][y][a] = 0

            for i in range(n):
                for j in range(n):
                    for k in range(2):
                        if arr[i][j][k]:
                            if k == gi:
                                if not gi_can(i,j,arr,bo,gi,n):
                                    arr[x][y][a] = 1
                            else:
                                if not bo_can(i,j,arr,bo,gi,n):
                                    arr[x][y][a] = 1


    for i in range(n):
        for j in range(n):
            for k in range(2):
                if arr[i][j][k]:
                    answer.append([i,j,k])

    return answer
