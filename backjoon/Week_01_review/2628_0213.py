# 2628 종이자르기

import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
N = int(input())

# 가로, 세로 길이를 저장할 리스트
x_list = [0, X]
y_list = [0, Y]
answer_list =[]
for i in range(N):
    tmp = list(map(int, input().split()))
    answer_list.append(tmp)
    if tmp[0] == 0:
        y_list.append(tmp[1])
    else:
        x_list.append(tmp[1])

x_list = sorted(x_list)
y_list = sorted(y_list)

x_max = 0
y_max = 0

for i in range(len(x_list)-1):
    if x_max < x_list[i+1] - x_list[i]:
        x_max = x_list[i+1] - x_list[i]

for i in range(len(y_list)-1):
    if y_max < y_list[i+1] - y_list[i]:
        y_max = y_list[i+1] - y_list[i]

print(x_max * y_max)