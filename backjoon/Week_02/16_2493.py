# 첫쨰줄에 탑의 수를 나타는 정수 N
import sys

N,k = int(input().split())
tower_li =  list(map(int, input()))

stack=[]
answer=[]

for i in range(N):
    
    while stack:
        if stack[-1][1] > tower_li[i]:
            answer.append(stack[-1][0]+1)
            break
        else:
            stack.pop()
            # 계속 대조 해서 적으면 계속 빼내는 과정
    if not stack:
        answer.append(0)
    stack.append([i, tower_li[i]])

print(" ".join(map(str, answer)))

# for i in range(1,N):
#     while stack:
#         # 스택에 값이 있을 때만 while문 진행한다.
#         if stack[-1][1] > tower_li[i]:
#             # 만약 스택의 맨뒤에 숫자가 타워의 i에ㅔ 있는 숫자보다 크다면
#             answer.append(stack[-1][0]+1)
#             break
#         else:
#             stack.pop()
#     if not stack:
#         answer.append(0)
#     stack.append([i, tower_li[i]])

# print(" ".join(map(str, answer)))

# for i in range(N):
    
#     while stack:
#         if stack[-1][1] > tower_li[i]:
#             answer.append(stack[-1][0]+1)
#             break
#         else:
#             stack.pop()
#     if not stack:
#         answer.append(0)
#     stack.append([i, tower_li[i]])
