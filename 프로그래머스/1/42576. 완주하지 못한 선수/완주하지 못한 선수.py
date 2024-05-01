def solution (participant, completion) :
    dict = {}
    for name in participant:
        dict[name] = dict.get(name,0)+1

    for i in completion:
        if i in dict:
            dict[i]-=1

    idx = [k for k, v in dict.items() if v>0]

    result = idx[0]

    return result