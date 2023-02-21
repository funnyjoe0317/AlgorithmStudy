# 골드바흐의 추축
import sys
import math
input = sys.stdin.readline

# N= int(input())
# num_list = []
# for i in range(N):
#     num_list.append(int(input()))

# # 소수 구하기
# prime = []
# for i in range(2, 10001):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         prime.append(i)

# answer = []
# for i in range(N):
#     for j in range(len(prime)):
#         if num_list[i] - prime[j] in prime:
#             answer.append((prime[j], num_list[i] - prime[j]))
#             break

# print(answer)

def d(N): # 소수 판별 함수
    if N == 1:
        return False
    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True
    
N = int(input()) # 테스트 케이스 수 입력

for _ in range(N):
    num = int(input()) # 짝수 입력
    
    A = num // 2 # 두 수 중 줄어드는 변수
    B = num // 2 # 두 수 중 늘어나는 변수
    
    for _ in range(num // 2):
        if d(A) and d(B): # 두 수가 소수이면 출력
            print(A, B)
            break
        else: # 소수가 아니면 두 수를 줄이고 늘리기
            A -= 1
            B += 1