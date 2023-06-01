from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    
    time_dic = {}
    fee_dic = defaultdict(int)
    max_time = 23*60 + 59
    
    for record in records:
        time, car, type = record.split()
        
        h, m = map(int, time.split(":"))
        time = h*60 + m
        
        if type == "IN":
            time_dic[car] = [time, True]
        else:
            fee_dic[car] += (time - time_dic[car][0])
            time_dic[car][1] = False
    
    car_list = []
    
    for car, value in time_dic.items():
        if value[1]:
            fee_dic[car] += (max_time - value[0])
        car_list.append((car, fee_dic[car]))
    
    car_list = sorted(car_list)
    for car, fee in car_list:
        if fee <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(math.ceil((fee-fees[0]) / fees[2]) * fees[3] + fees[1])
            
            
    
    
    return answer