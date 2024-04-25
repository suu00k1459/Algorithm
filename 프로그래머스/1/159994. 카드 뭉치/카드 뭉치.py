def solution(cards1, cards2, goal):
    
    a ,b = cards1.pop(0), cards2.pop(0)

    for i in goal:
        
        if i == a:
            if len(cards1)==0:
                a = 0
            else :
                a = cards1.pop(0)
        elif i == b:
            if len(cards2) ==0:
                b = 0
            else :
                 b = cards2.pop(0)
        else :
            return "No"
    return "Yes"