# 연산자 끼워넣기 0219
# import sys
# import itertools

# input = sys.stdin.readline

# N = int(input())

# kiho = {
#     "+" :0,
#     "-" : 0,
#     "*":0,
#     "//":0
# }

# num_list = list(map(int, input().split()))
# print(num_list)
# kiho_list = list(map(int, input().split()))
# print(kiho_list)

# kiho["+"] = kiho_list[0]
# kiho["-"] = kiho_list[1]
# kiho["*"] = kiho_list[2]
# kiho["//"] = kiho_list[3]
# # print(kiho)

# # sorted_ops = [k for k, v in sorted(kiho.items(), key=lambda x: x[1])]

# # print(sorted_ops)

# key_list =[]
# for key, value in kiho.items():
    
#     key_list.extend([key] * value)

# print(key_list)
# answer_list = []

# answer = 0
# tmp = 0
# for i in itertools.permutations(key_list, len(key_list)):
#     for j in i:
#         if i[j] =="+":
#             tmp = num_list[j] + num_list[j+1]
#         elif i[j] =="-":
#             tmp = num_list[j] - num_list[j+1]
#         elif i[j] =="*":
#             tmp = num_list[j] * num_list[j+1]
#         else:
#             tmp = num_list[j] // num_list[j+1]
#     answer_list.append(tmp)

# print(max(answer_list))
# print(min(answer_list))

# 쳇 지피티가 개선해준 코드

import sys
import itertools

input = sys.stdin.readline

N = int(input())

kiho = {
    "+": 0,
    "-": 0,
    "*": 0,
    "//": 0
}

num_list = list(map(int, input().split()))
kiho_list = list(map(int, input().split()))

kiho["+"] = kiho_list[0]
kiho["-"] = kiho_list[1]
kiho["*"] = kiho_list[2]
kiho["//"] = kiho_list[3]

key_list = []
for key, value in kiho.items():
    key_list.extend([key] * value)


max_value, min_value = float('-inf'), float('inf')
answer_list = []
for i in itertools.permutations(key_list, len(key_list)):
    tmp = num_list[0]
    for j in range(len(i)):
        if i[j] == "+":
            tmp += num_list[j+1]
        elif i[j] == "-":
            tmp -= num_list[j+1]
        elif i[j] == "*":
            tmp *= num_list[j+1]
        else:
            tmp = int(tmp / num_list[j+1])
    max_value = max(max_value, tmp)
    min_value = min(min_value, tmp)

print(max_value)
print(min_value)


# 더 개선하여DFS로 풀이 왜 빠를까?
import sys

input = sys.stdin.readline

N = int(input())

kiho = ["+", "-", "*", "/"]
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

max_value = float('-inf')
min_value = float('inf')

def dfs(op_idx, cur_value):
    global max_value, min_value

    if op_idx == N-1:
        max_value = max(max_value, cur_value)
        min_value = min(min_value, cur_value)
        return

    for i in range(4):
        if ops[i] > 0:
            ops[i] -= 1

            if i == 0:
                dfs(op_idx+1, cur_value+nums[op_idx+1])
            elif i == 1:
                dfs(op_idx+1, cur_value-nums[op_idx+1])
            elif i == 2:
                dfs(op_idx+1, cur_value*nums[op_idx+1])
            else:
                dfs(op_idx+1, int(cur_value/nums[op_idx+1]))

            ops[i] += 1

dfs(0, nums[0])

print(max_value)
print(min_value)