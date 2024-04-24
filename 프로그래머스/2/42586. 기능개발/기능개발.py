import math
def solution(progresses, speeds):
    answer = []
    a=0
    day=0
    day_list=[]

    for i in range(len(progresses)):
        a= 100 - progresses[i] 
        day = math.ceil(a/speeds[i])
        day_list.append(day)
        print("day",day)
    print(day_list)
    
    cnt = 1  #3
    max_day = day_list[0] 
    for j in range(1, len(day_list)):
        if day_list[j] <= max_day: 
            cnt += 1
        else:  
            answer.append(cnt)
            print(cnt)
            cnt = 1
            
            max_day = day_list[j]   
    answer.append(cnt) 
    return answer