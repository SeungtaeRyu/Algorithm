import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    num = ""
    
    while n > 0:
        num = str(n % k) + num
        n //= k
    
    numbers = num.split('0')
    for number in numbers:
        if number != '' and is_prime(int(number)):
            answer += 1
    
    return answer