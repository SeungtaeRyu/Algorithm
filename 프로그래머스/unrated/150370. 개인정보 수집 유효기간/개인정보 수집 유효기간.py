def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    
    for term in terms:
        a, b = term.split()
        terms_dict[a] = int(b)
    
    todayy = list(map(int, today.split(".")))
    x = [todayy[0]*12 + todayy[1], todayy[2]]
    
    i = 1
    for privaciy in privacies:
        term = privaciy.split()
        termm = list(map(int, term[0].split(".")))
        termm[1] += terms_dict[term[1]]
        
        y = [termm[0]*12 + termm[1], termm[2]]
        if x[0] > y[0]:
            answer.append(i)
        elif x[0] == y[0] and x[1] >= y[1]:
            answer.append(i)          
        i += 1

    
    return answer