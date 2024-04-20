def solution(prices):
    lst=[]
    for i in range(len(prices)):
        s = 0
        for j in range(i+1,len(prices)):
            if prices[i]<=prices[j]:
                 s+=1
            else:
                s+=1
                break
        lst.append(s)
    return lst