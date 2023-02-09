# 내 풀이
def solution(nums):
    d = {}
    answer = 0

    for i in nums:
        if i not in d:
            d[i] = True
            #굳이 이렇게 안하고 set으로 바꿔서 len(set(nums)) 해도 됨 

    if len(d) >= len(nums)//2:
        answer = len(nums)//2
    else:
        answer = len(d)

    return answer




# 다른 사람풀이
def solution(ls):
    return min(len(ls)/2, len(set(ls)))