def solution(n, k):
    answer = -1
    num_lst = []
    # 기능 1 : 3 ~ 10진수를 만들어 주는 코드
    while n > 0:
        tmp = n % k
        num_lst.append(str(tmp))
        n = n // k
    
    # print(num_lst)
    num_lst="".join(num_lst[::-1])
    # print(num_lst)
    parts = num_lst.split('0')
    new_parts = [int(x) for x in parts if x != ''] # 빈 문자열 제거
    # print(new_parts)
    
    def is_prime(n):
        if n<2:
            return False
        for i in range(2, int(n ** 0.5)+1):
            if n % i == 0:
                return False
        return True
    
    cnt = 0
    
    for s in new_parts:
        if is_prime(s):
            cnt +=1
    
    
    return cnt