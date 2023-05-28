from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    
    n = len(emoticons)
    digits = [10, 20, 30, 40]

    for combination in product(digits, repeat=n):
        
        sign_count = 0
        revenue = 0
        for user in users:
            temp_revenue = 0
            for i in range(n):
                if user[0] <= combination[i]:
                    temp_revenue += (emoticons[i] - emoticons[i] * combination[i] * 0.01)
                if temp_revenue >= user[1]:
                    sign_count += 1
                    break
            else:
                revenue += temp_revenue
        
        if sign_count > answer[0]:
            answer[0] = sign_count
            answer[1] = revenue
        elif sign_count == answer[0]:
            answer[1] = max(answer[1], revenue)
        
        
                    
            
    
    
    return answer