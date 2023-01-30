# 모든 원소의 값이 0보다 크거나 같다고 가정
import sys
input = sys.stdin.readline

n = int(input())
# sorting_list = list(map(int, input().split()))
sorting_list =[0]*10001
# 메모리(저장공간을 미리 할당하는 이유: 컴퓨터의 경우 메모리를 가변형(범위를 제한을 안할경우 메모리를 알아서 2배정도 늘릴 수 잇다 )그래서 더 많이 질수 있기에 미리 할당)

for _ in range(n):
    number =int(input())
    sorting_list[number] +=1

for i in range(10001):
    if sorting_list[i] != 0:
        for j in range(sorting_list[i]):
            print(i)






# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
# count = [0] * (max(sorting_list) + 1)
# for i in range(len(sorting_list)):
#     count[sorting_list[i]] += 1 
#     # 각 데이터에 해당하는 인덱스의 값 증가

# for i in range(len(count)):
#     # 리스트에 기록된 정렬 정보 확인
#     for j in range(count[i]):
#         print(i) 
#         # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력