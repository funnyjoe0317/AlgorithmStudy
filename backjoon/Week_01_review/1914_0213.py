# 1914_하노이 탑

import sys
input = sys.stdin.readline

N = int(input())

def hanoi(n, start, end):
    if n == 1:
        print(start, end)
    else:
        hanoi(n-1, start, 6-start-end)
        print(start, end)
        hanoi(n-1, 6-start-end, end)

print(2**N-1)
if N <= 20:
    hanoi(N, 1, 3)
else:
    pass




# cnt =0
# # 하노이 탑 구현하기
# def move(no, x, y):
#     global cnt
#     if no > 1:
#         move(no-1, x, 6-x-y)

#     # print(f'원반 [{no}]을 {x}기둥에서 {y}기둥으로 옮깁니다.')
#     if no < 20:
#         # print(f'{x} {y}')
#     cnt +=1

#     if no > 1:
#         move(no - 1, 6-x-y, y)

# N = int(input())
# print(cnt)
# if N < 20:
#     move(N,1,3)
