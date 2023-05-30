def rotate(key):
    n = len(key)
    new_key = [[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            new_key[j][n-1-i] = key[i][j]
    return new_key

def solution(key, lock):
    answer = False
    n = len(key)
    m = len(lock)
    
    # 회전 4번하기
    for _ in range(4):
        key = rotate(key)
        # 가로
        for i in range(-n, m+1):
            # 세로
            for j in range(-n, m+1):
                
#                 new_map = [[0 for i in range(m)] for i in range(m)]
#                 print("i = ",i, "j = ", j)
#                 for k in range(m):
#                     for l in range(m):
#                         if 0 <= k-i < n and 0 <= l-j < n:
#                             new_map[k][l] = lock[k][l] + key[k-i][l-j]
#                         else:
#                             new_map[k][l] = lock[k][l]
                            
#                 for a in new_map:
#                     print(a)
#                 print()

#                 for k in range(m):
#                     for l in range(m):
#                         if new_map[k][l] != 1:
#                             break
#                     else:
#                         continue
#                     break
#                 else:
#                     print("성공")
                
                
                # 모든칸 검사
                for k in range(m):
                    for l in range(m):
                        if 0 <= k-i < n and 0 <= l-j < n:
                            if lock[k][l] + key[k-i][l-j] != 1:
                                break
                        else:
                            if lock[k][l] != 1:
                                break
                    # 한줄동안 브레이크를 만나지 않으면
                    else: 
                        continue
                    # 브레이크를 만났으면
                    break
                # 모든줄 동안 브레이크를 만나지 않으면
                else:
                    return True
    
    return answer