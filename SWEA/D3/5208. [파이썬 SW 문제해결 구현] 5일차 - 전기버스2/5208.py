

# n = 5, battery = [2, 3, 1, 1]

# step1. dp = [-1, -1, -1, -1, -1] 로 초기화
# step2. 이전에 방문하지 않은 dp만 갱신한다! (dp[k] != -1이 아닐때)
#           battery[0] = 2이므로 dp[1]과 dp[2]가 갱신됨 dp[0]+1로 하면 됨!
#               => dp = [-1, 0, 0, -1, -1]
#           battery[1] = 3이므로 dp[2]과 dp[3]과 dp[4]가 갱신됨 dp[1]+1로 하면 됨!
#               => dp = [-1, 0, 0, 1, 1]
#           ...
# step3. step2의 과정을 battery의 length만큼 반복한다.
# step4. 과정 반복 중 dp[n-1]의 값이 기록될 경우 모든 작업을 중단하고 정답을 출력한다.

T = int(input())
for tc in range(1, T+1):
    n, *battery = map(int, input().split())

    dp = [-1] * n
    for i in range(len(battery)):                   # 충전소의 길이만큼 반복문 동작
        for j in range(1, battery[i]+1):                # 해당 충전소의 충전가능 위치만큼 반복문 동작
            if dp[i+j] == -1:                               # 한번도 방문한 적이 없다면 dp[i+j] 갱신
                dp[i+j] = dp[i] + 1
            if i+j == n-1:                                  # i+j가 n-1에 도착하면 dp[n-1]이 채워진 상태!
                break                                       # 2중 for 문 탈출!
        else:
            continue
        break
    print(f'#{tc} {dp[n-1]}')                               # dp[n-1] 출력

