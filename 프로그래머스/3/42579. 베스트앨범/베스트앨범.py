def solution(genres, plays):
    dict = {}
    for i in range(len(genres)):
        dict[genres[i]] = dict.get(genres[i],0)+ plays[i]

    dict = sorted(dict.items(), key = lambda x : -x[1])

    temp = []
    for i in dict:
        lst = []
        for j in range(len(genres)):
            if i[0] == genres[j]:
                lst.append([j, plays[j]])
        
        lst = sorted(lst, key = lambda x: -x[1])

        if len(lst)>2:
            k = 2
        else :
            k = len(lst)
            
        for i in range(k):
            temp.append(lst[i][0])
        
    return temp 

