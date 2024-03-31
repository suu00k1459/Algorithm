def solution(q,r, code):
    rst=[]
    for i in range(len(code)):
        if i%q ==r:
            rst.append(code[i])
    return ''.join(rst)