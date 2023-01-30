import sys
input = sys.stdin.readline

# N,K = map(int,(input().split()))
# X = sorted([int(input().rstrip()) for _ in range(N)])

# l, r = min(X), max(X)+K

# def calc(lst, m):
#     t = 0
#     for num in lst:
#         if num >= m:
#             break
#         t += m-num
#     return t

# while l <= r:
#     m = (l+r)//2
#     if calc(X,m) <= K:
#         res = m
#         l = m+1
        
#     else:
#         r = m-1

# print(res)

import sys
input = sys.stdin.readline

n, k = map(int,input().split())
levels = [ int(input()) for _ in range(n)]

start = min(levels)
end = start + k

res = 0
# 전 미드값과 대조하기 위해 미리 설정
while start <= end:
    # 목표는 start와 end값이 같아지는 지점을 만드는게 목표
    # 그러기 위해서는 스타트와 엔드값이 같아지게 +-를 해주는게 중요
    mid = (start + end) // 2
    
    hap = 0
    for level in levels:
        if mid > level:
           hap+= (mid - level)
        # 이 hap 이 같아지게 커지게 된다면 미드값과 
        # 엔드값이 너무 뒤에 왔다는 의미이고
        # hap이K보다 작다면 반대로 스타트와 앤드가 아직
        # 더 커져야한다는 의미   
           
    if hap <= k:
        start = mid+1
        res = max(mid,res)
        # res는 이전값이 맞는 경우이기 mid값이 작아져 코드가 다시도는 일없게 하기
    else:
        end = mid -1


print(res)