from collections import deque
import itertools

def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        # numbers = [4, 1, 2, 1]
        tmp = []
        for parent in leaves:
            # leaves = [0]
            tmp.append(parent + num)
            # 
            tmp.append(parent - num)
        leaves = tmp
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer



def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])


from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
# def solution(numbers, target):
#     queue = deque()
#     queue.append(numbers)
#     visited = [False] * len(numbers)
#     answer = 0
#     while queue:
#         for i in range(len(numbers)):
#             curr_list = queue.popleft()

#             if sum(curr_list) == target:
#                 answer += 1
#                 visited[i] = True
#                 new_list = curr_list[:]
#                 for j in range(i, len(curr_list)):
#                     new_list[j] = -new_list[j]
#                     new_list[j-1] = -new_list[j-1]
#                     if sum(curr_list) == target:
#                         answer += 1
#                 curr_list[i] = -curr_list[i]
#                 queue.append(curr_list)

#             else:
#                 curr_list[i] = -curr_list[i]
#                 visited[i] = True
#                 queue.append(curr_list)
#                 if sum(visited) == len(numbers):
#                     return answer
                
#     # return answer

# def solution(numbers, target):
#     queue = deque()
#     queue.append(numbers)
#     visited = [False] * len(numbers)
#     answer = 0
#     while queue:
#         for i in range(len(numbers)):
#             curr_list = queue.popleft()

#             if sum(curr_list) == target:
#                 answer += 1
#                 visited[i] = True
#                 new_list = curr_list[:]
#                 for j in range(i, len(curr_list)):
#                     new_list[j] = -new_list[j]
#                     new_list[j-1] = -new_list[j-1]
#                     if sum(curr_list) == target:
#                         answer += 1
#                 curr_list[i] = -curr_list[i]
#                 queue.append(curr_list)

#             else:
#                 curr_list[i] = -curr_list[i]
#                 visited[i] = True
#                 queue.append(curr_list)
#                 if sum(visited) == len(numbers):
#                     return answer


numbers = [4,1,2,1]
target = 4
print(solution(numbers, target))
