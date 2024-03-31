def solution(n, i, num_list):
    if n ==1:
        return num_list[:i[1]+1]
    elif n==2:
        return num_list[i[0]:]
    elif n==3:
        return num_list[i[0]:i[1]+1]
    else :
        return num_list[i[0]:i[1]+1:i[2]]