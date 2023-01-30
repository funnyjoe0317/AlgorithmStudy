
import sys

input = sys.stdin.readline
n,c = map(int, input().split())
h=[int(input()) for i in range(n)]
h.sort()
start, end = 1, h[n-1] - h[0]
# 이분탐색의 기본으로 시작값과 끝값을 정해준다
result =0

if c==2:
    # 공유기 두개 설치의 경우 자동으로 맨앞과 맨뒤의 거리가 정답
    print(h[n-1]-h[0])

else:
    while(start <end):
        mid = (start +end)//2
        # 거리를 나눈다 라는 개념이 이분탐색
        count = 1
        distanc_e = h[0]
        # [1,2,4,8,9]
        for i in range(n):
            if h[i] - distanc_e >= mid:
                count += 1
                distanc_e = h[i]
                # 거리를 하나하나 전체 거리를 나눈 mid값으로 대조 한다. 
        if count >= c:
            result = mid
            start = mid + 1
            # 공유기의 거리가 안나오면 다시 스타트 값을 조정하여 while 문으로
        elif count < c:
            end = mid
    print(result)
