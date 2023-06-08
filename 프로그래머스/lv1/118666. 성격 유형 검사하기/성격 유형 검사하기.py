def solution(survey, choices):
    # 1 매우 비동   3점
    # 2 비동       2점
    # 3 약간 비동   1점
    # 4 중립       0점
    # 5 약간 동의   1점
    # 6 동의       2점
    # 7 매우 동의   3점
    type = ["A", "N", "R", "T", "C", "F", "J", "M"]
    scores = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    dic = {"A": 0, "N": 0, "R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0}
    for i in range(len(survey)):
        if choices[i] > 4:
            dic[survey[i][1]] += scores[choices[i]]
        else:
            dic[survey[i][0]] += scores[choices[i]]
            
    answer = ['R','C','J','A']
    
    if dic["N"] > dic["A"]:
        answer[3] = 'N'
    if dic["T"] > dic["R"]:
        answer[0] = 'T'
    if dic["F"] > dic["C"]:
        answer[1] = 'F'
    if dic["M"] > dic["J"]:
        answer[2] = 'M'
        
        
    return "".join(answer)