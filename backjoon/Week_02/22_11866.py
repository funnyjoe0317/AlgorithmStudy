from collections import deque
import sys
input = sys.stdin.readline
# # 집의 개수와 공유기 설치 대수
# N = list(map(int, input().split()))
# Qnumber_li = deque([])

# for i in range(1,N[0]+1):
#     Qnumber_li.append(i)

# for i in range(len(Qnumber_li)):
#     for j in range(2):
#         pop

N,K = map(int,input().split())
# 두개 받을 때 
arr = [i for i in range(1,N+1)]
# 한번에 원하는 숫자까지 만들어주는 방법
dead_li = []
num = 0

for i in range(N):
    num += K-1
    if num >= len(arr):
        num = num%len(arr)

    dead_li.append(str(arr.pop(num)))

print("<",", ".join(dead_li)[:],">", sep='')

    
