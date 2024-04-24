import math

def solution(progresses, speeds):
    answer = []
    a=0
    day=0
    day_list=[]

    for i in range(len(progresses)):
      a= 100 - progresses[i] 
      day = a/speeds[i] #여기서 오류떴었음 -> 반례가 있었음, 처음에는 a//speeds[i]해서 몫만 구해졌던거
      day = math.ceil(day)
      day_list.append(day)
    print(day_list)
    
    cnt = 1  
    max_day = day_list[0] 
    for j in range(1, len(day_list)):
        if day_list[j] <= max_day: 
            cnt += 1
        else:  
            answer.append(cnt)
            cnt = 1
            max_day = day_list[j]
            
    answer.append(cnt) 
    return answer