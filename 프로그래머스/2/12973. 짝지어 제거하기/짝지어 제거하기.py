def solution(s):
    lst = []
    for i in s:
        if len(lst) == 0:
            lst.append(i)
        else:
            if i== lst[-1]:
                lst.pop()
            else :
                lst.append(i)
    
    
    if len(lst) != 0:
        return 0
    else :
        return 1