def get_distinct_input(n, m):
    result = set()
    for _ in range(n):
        myInput = input().strip()
        if myInput != '0'*m:
            result.add(myInput)
    return list(result)

def get_16_to_2(arr_16):
    hextobin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111', }
    result = []
    for i in range(len(arr_16)):
        word_2 = ''
        for j in range(len(arr_16[i])):
            word_2 += hextobin[arr_16[i][j]]
        result.append(word_2)
    return result

def get_amho(arr_2):
    pattern = {'211': '0', '221': '1', '122': '2', '411': '3', '132': '4',
                 '231': '5', '114': '6', '312': '7', '213': '8', '112': '9', }
    result = set()
    for i in range(len(arr_2)):         # 중복제거된 입력을 한줄 한줄 실행
        count = 0                                   # step1. 뒤에서 부터 0과 1의 개수를 세어서 스택에 카운트
        state = '0'
        stack = []
        for j in range(len(arr_2[i]) - 1, -1, -1):
            if arr_2[i][j] == state:
                count += 1
            else:
                state = arr_2[i][j]
                stack.append(count)
                count = 1

        pattern_amho = []                           # step2. 3자리를 꺼내서 패턴을 읽고, 한자리를 더 꺼내서 버림
        for _ in range(len(stack) // 4):                        # pattern_amho 는 [[3, 1, 2], [2, 1, 1], ...] 이런 구조로 들어갈 예정
            pattern_temp = []                                   # pattern_temp 는 [3, 1, 2] 이런 구조
            for i in range(3):
                pattern_temp.append(int(stack.pop()))
            pattern_amho.append(pattern_temp)
            stack.pop()

        amho = ''                                   # step3. 리턴할 암호코드로 변환하기
        for i in range(len(pattern_amho)):
            temp = ''
            for j in range(3):                                  # [3, 1, 2] 자리를 각각 min 으로 나눈 후 스트링으로 더함
                temp += str(int(pattern_amho[i][j]) // min(pattern_amho[i]))
            amho += pattern[temp]                               # '312'의 패턴을 매칭해서 암호코드 구하기

            if i % 8 == 7:                                      # 암호코드가 8자리가 되면 리턴할 set 에 add 하기
                result.add(amho)
                amho = ''
    return list(result)

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    arr_16 = get_distinct_input(n, m)   # step1. 16진수 input 입력 받기 + 중복 제거
    arr_2 = get_16_to_2(arr_16)         # step2. 16진수 -> 2진수로 변환
    amho_list = get_amho(arr_2)         # step3. 2진수 -> 암호코드 해석

    ans = 0                             # step4. 암호 검증
    for i in range(len(amho_list)):
        temp_ans = 0
        total = 0
        for j in range(8):
            if j % 2:
                total += int(amho_list[i][j])
                temp_ans += int(amho_list[i][j])
            else:
                total += int(amho_list[i][j])*3
                temp_ans += int(amho_list[i][j])
        if total % 10 == 0:
            ans += temp_ans

    print(f'#{tc} {ans}')               # 정답 출력