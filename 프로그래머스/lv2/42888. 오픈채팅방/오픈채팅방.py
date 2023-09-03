from collections import defaultdict

def solution(record):
    answer = []
    uid_dic = defaultdict(str)
    
    for r in record:
        t, uid, *name = r.split()
        if name:
            uid_dic[uid] = name[0]
    
    for r in record:
        t, uid, *name = r.split()
        if t == "Enter":
            answer.append(uid_dic[uid] + "님이 들어왔습니다.")
        elif t == "Leave":
            answer.append(uid_dic[uid] + "님이 나갔습니다.")

    
    return answer