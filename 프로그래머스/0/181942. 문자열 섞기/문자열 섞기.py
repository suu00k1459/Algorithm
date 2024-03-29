def solution(str1, str2):
    return ''.join([a1+b1 for a1,b1 in zip(str1, str2)])