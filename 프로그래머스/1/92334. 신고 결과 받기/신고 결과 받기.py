def solution(id_list, report, k):
    id_dict={}
    rep_dict ={}

    for i in id_list:
        id_dict[i]=0
        rep_dict[i] =0

    for j in list(set(report)):
        n,r = j.split(" ")
        rep_dict[r] +=1
        
    ky = [ky for ky, v in rep_dict.items() if v>=k]

    for j in list(set(report)):
        n,r = j.split(" ")
        for i in ky:
            if r == i:
                id_dict[n] +=1

    return list(id_dict.values())