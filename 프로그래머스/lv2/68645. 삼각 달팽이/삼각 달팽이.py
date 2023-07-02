def solution(n):
    answer = []
    arr = []
    direction = [(1, 0), (0, 1), (-1, -1)]
    
    for i in range(1, n+1):
        arr.append([0 for _ in range(1, i+1)])
    
    d_index = 0
    x, y = -1, 0
    num = 1
    
    while n != 0:
        for i in range(n):
            x += direction[d_index][0]
            y += direction[d_index][1]
            arr[x][y] = num
            num += 1
        n -= 1
        
        if d_index == 2:
            d_index = 0
        else:
            d_index += 1
    
    for i in arr:
        for j in i:
            answer.append(j)
    
    return answer