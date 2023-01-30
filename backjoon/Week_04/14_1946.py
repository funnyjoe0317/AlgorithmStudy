# 신입 사원
# 채용을 할 때 면접 성적과 시험 성적 중 적어도 하나가 다른 지원자보다
# 떨어지지 않는 자만 선발 한다는 원칙을 세웠다. 

# 예시 5명의 지원자
# 3 2 점수
# 1 4 점수

# import sys

# input = sys.stdin.readline
# n = int(input())
# student_li = []
# for i in range(n):
#     r = int(input())
#     for k in range(r):
#         student_li.append(list(map(int, input().split())))
#     # student_li.sort(key = lambda x: x[0])
#     student_li.sort()
#     min_rank = student_li[0][1]
#     cnt = 1
#     for j in range(r):
#         rank = student_li[j][0]
#         if rank < min_rank:
#             min_rank =rank
#             cnt +=1
# print(cnt)





# 답지의 생각
# 첫 번째 서류심사 성적으로 정렬, 두번째 점수인 면접 성적을 비교해서 합격자
# 간단한디 두번째가 까다로움 
# 자신보다 서류심사 성적이 높은 면접자들의 면접 성적보다  자기자신의 성적이 
# 높아야한다. 

import sys
input = sys.stdin.readline
T = int(input())

for i in range(T) :
    n = int(input())
    people_lst = [0]*n
    for j in range(n) :
            t1 ,t2 = map(int,input().split())
            people_lst[j] = [t1,t2]

    people_lst_sorted_0 = sorted(people_lst, key = lambda x : x[0])
    hired = 1
    man = people_lst_sorted_0[0][1]
    for j in range(1,n) :
        if people_lst_sorted_0[j][1] < man :
            man = people_lst_sorted_0[j][1]
            hired += 1

    print(hired)

import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    rank = [list(map(int, input().split())) for _ in range(N)]
    rank_asc = sorted(rank)
    top = 0
    result = 1
    
    for i in range(1, len(rank_asc)):
        if rank_asc[i][1] < rank_asc[top][1]:
            top = i
            result += 1
    
    print(result)