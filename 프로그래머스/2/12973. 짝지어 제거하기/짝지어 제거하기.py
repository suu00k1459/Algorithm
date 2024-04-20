

def solution(s):
    lst =list(s)
    while True:
        for i in range(0,len(lst)-1):
            if lst[i]==lst[i+1]:
                lst.pop(i+1)
                lst.pop(i)
                break
            else :
                pass

            if i==len(lst)-2:
                return 0
                
        if len(lst)==0:
            return 1
        