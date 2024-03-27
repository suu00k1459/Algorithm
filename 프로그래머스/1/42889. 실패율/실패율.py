def solution(N, stages):
    clg = len(stages)
    f=[]
    result=[]
    
    for i in range(1,N+1):
        st = stages.count(i)
        if st ==0:
            f.append((0,i))
        else :
            f.append((st/clg,i))
            clg-= st
    f.sort(key= lambda x : (-x[0],+x[1]))
    
    for i in f:
        result.append(i[1])
    return result