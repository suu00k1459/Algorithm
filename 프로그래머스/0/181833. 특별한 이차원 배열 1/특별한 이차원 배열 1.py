def solution(n):
    answer=[]
    for i in range(n): #0,1,2
        lst=[]
        for j in range(n) : #0,1,2    
            if i==j:
                lst.append(1)
            else:
                lst.append(0)
        answer.append(lst)
    return answer