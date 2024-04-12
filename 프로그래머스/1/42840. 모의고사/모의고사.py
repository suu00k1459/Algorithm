import math

def solution(ans):
    a = [1,2,3,4,5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    a = (a*math.ceil(len(ans)/len(a)))[:len(ans)]
    b = (b*math.ceil(len(ans)/len(b)))[:len(ans)]
    c = (c*math.ceil(len(ans)/len(c)))[:len(ans)]

    dct ={1:0,2:0,3:0}
    
    for i in range(len(ans)):
        if ans[i] == a[i]:
            dct[1]+=1
        if ans[i] == b[i]:
            dct[2]+=1
        if ans[i] == c[i]:
            dct[3]+=1
            
    return [k for k, v in dct.items() if v == max(dct.values())]