# 블랙잭
import sys
import itertools
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
answer = -sys.maxsize - 1
# answer_list =[]
for i in itertools.combinations(num_list, 3):
    if sum(i) > M:
        # print(sum(i))
        continue
    elif answer <= sum(i):
        answer = sum(i)
        # answer_list = i
        
print(answer)
