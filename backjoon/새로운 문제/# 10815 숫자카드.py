# 10815 숫자카드
# A : 5 3 2 5
# B : 5 2 1 5
# 답: 1 0 0 1 
 
import sys
input= sys.stdin.readline

A = input()
num_list_1 = list(map(int, input().split()))
num_list_1.sort()


B = input()
num_list_2 = list(map(int, input().split()))

# 일반 받아놓고 확인하기 하나씩 확인하기 n*n번 확인해야한다. n^2?
# ans_list =[]
# # print(num_list_1,  num_list_2)
# for i in range(len(num_list_2)):
#     if num_list_2[i] in num_list_1:
#         ans_list.append(1)
#         # print("1 ")
#     else:
#         ans_list.append(0)
#         # print("0 ")

# print(*ans_list)

# 이진탐색으로 찾기

def binary_search(num_list, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if num_list[mid] == target:
            return 1    
        elif num_list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in range(len(num_list_2)):
    print(binary_search(num_list_1, num_list_2[i], 0, len(num_list_1)-1), end=" ")
    
# print(*ans_list)

# binary_search(num_list_1, num_list_2[i], 0, len(num_list_1)-1)

