def solution(my_string, queries):
    st = list(my_string)
    for i in queries:
        st[i[0]:i[1]+1] = st[i[0]:i[1]+1][::-1]
    return ''.join(st)