def solution(str_list):
    def fd(st_list,i):
        try:
            a = str_list.index(i)
        except ValueError:
            a = len(st_list)
        return a
    
    if fd(str_list,"l") < fd(str_list,"r"):
        return str_list[:fd(str_list,"l")]
    else :
        return str_list[fd(str_list,"r")+1:]