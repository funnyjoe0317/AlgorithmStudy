# 차이를 최대로 0217

import sys
import itertools
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
tmp, answer = 0, 0

answer_list = itertools.permutations(arr, len(arr))

for i in answer_list:
    tmp = 0
    for j in range(len(i)-1):
        tmp += abs(i[j]- i[j+1])
        if tmp > answer:
            answer = tmp


print(answer)
# for i in itertools.combinations(arr):
#     # [ 20 1 15 8 4 10 ]
#     answer += abs(arr[i] - arr[i+1])

# print(answer)
