def solution(want, number, discount) :
    t=0
    for i in range(len(discount)-9):
        temp = discount[i:i+10]
        dict = {}
        for j in temp :
            dict[j] = dict.get(j,0)+1

        s = True
        for i in range(len(want)):
            if  want[i] in dict:
                if number[i] <= dict[want[i]]:
                    s = True
                else:
                    s = False
                    break
            else:
                s = False
                break
        if s == True:
            t+=1
            
    return t