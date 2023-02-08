# 평균은 넘겠지
import sys
input = sys.stdin.readline

C = int(input())

for i in range(C):
    case = list(map(int, input().split()))
    answer = 0
    cnt = 0
    for j in range(1,len(case)):
        answer += case[j]
    answer = answer/case[0]
    print(answer)
    for j in range(1,len(case)):
        if case[j] > answer:
            cnt += 1
    print("%.3f" % (cnt/case[0]*100) + "%")

# for i in range(C):
#     answer = 0
#     case = list(map(int, input().split()))
#     print(case)
#     for j in range(1,len(case)):
#         answer += case[j]
#         print(answer)

    
#     answer = answer/case[0]
#     print(answer)
#     for j in range(1,len(case)):
#         if case[j] > answer:
#             answer += 1
        
#     print(answer/case[0])