def solution(board, moves):
    temp = []
    s=0
    for i in moves:
        for j in board:
            if j[i-1] ==0:
                pass
            else:
                temp.append(j[i-1])
                if len(temp)>=2:
                    if temp[-1] == temp[-2]:
                        temp.pop()
                        temp.pop()
                        s+=2
                    
                j[i-1]=0
                break
    return s
