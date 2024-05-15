def solution(numbers, hand):
    answer = ''
    l, r = "*", "#" # 왼쪽, 오른쪽 엄지 위치
    lefts = [1, 4, 7, "*"] # 왼쪽 엄지로 쳐야하는 숫자들
    rights = [3, 6, 9, "#"] # 오른쪽 엄지로 쳐야하는 숫자들
    middles = [2, 5, 8, 0]
    
    for n in numbers:
        if n in lefts: # n이 (1, 4, 7)에 해당될 때
            answer += "L"
            l = n 
        elif n in rights: # n이 (3, 6, 9)에 해당될 때
            answer += "R"
            r = n 
        else: # n이 (2, 5, 8, 0)에 해당될 때
            m = middles.index(n) # middles에서 n의 인덱스
            if l in lefts:
                idx_l = lefts.index(l)
                diff_l = abs(m - idx_l)
            else: # 왼쪽 엄지가 (2, 5, 8 ,0)에 있을 수도 있다. 
                idx_l = middles.index(l) 
                diff_l = abs(m - idx_l) - 1
            if r in rights:
                idx_r = rights.index(r)
                diff_r = abs(m - idx_r)
            else: # 오른쪽 엄지가 (2, 5, 8 ,0)에 있을 수도 있다. 
                idx_r = middles.index(r) 
                diff_r = abs(m - idx_r) - 1
            
            if diff_l < diff_r:
                answer += "L"
                l = n
            elif diff_l > diff_r:
                answer += "R"
                r = n
            else: # 왼쪽 엄지나 오른쪽 엄지나 거리 차이가 없을 때
                if hand == "left":
                    answer += "L"
                    l = n
                else:
                    answer += "R"
                    r = n
            
    return answer