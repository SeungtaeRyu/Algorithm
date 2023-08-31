def change(num, n):
    # 10부터 15까지의 숫자에 대한 매핑
    digits = "0123456789ABCDEF"

    # 변환 결과를 저장할 빈 문자열 초기화
    result = ""

    # 0에 대한 예외 처리
    if num == 0:
        return "0"

    while num > 0:
        # 나머지를 구하고 해당 진수 숫자를 결과에 추가
        remainder = num % n
        result = digits[remainder] + result

        # 나누기 연산을 통해 다음 자릿수로 이동
        num = num // n

    return result


def solution(n, t, m, p):
    answer = ''
    num = 0
    count = 0

    while True:
        result = change(num, n)
        for r in result:
            count += 1
            if count == p:
                answer += r
            if count == m:
                count = 0
        if len(answer) >= t:
            break
        num += 1


    return answer[:t]