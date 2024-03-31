def solution(myStr):
    rst = list(filter(None, myStr.replace("b","a").replace("c","a").split("a")))
    if len(rst)==0:
        rst.append("EMPTY")
    
    return rst
