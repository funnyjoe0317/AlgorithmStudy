# 주사위 굴리기
# import sys
# input = sys.stdin.readline

# N, M, x, y, K = map(int, input().split())
# # print(N, M, x, y, K)
# bitmap = []
# for i in range(N):
#     bitmap.append(list(map(int, input().split())))
# # print(bitmap)

# command = list(map(int, input().split()))
# # print(command)

# # dice 만드는 과정
# my_dice = {key:0 for key in range(1,7)}
# com = 2


# # for i in command:
# #     rolling()
    
# def rolling(dice, i,x,y,com):
    
#     # 1은 동쪽
#     if i == 1 and bitmap[y][x-1]:
#         x = x-1
#         # com = 
#     # 2는 서쪽
#     elif i == 2 and bitmap[y][x+1]:
#         x = x+1
#     elif i == 3 and bitmap[y-1][x]:
#         y = y-1
#     elif i  == 4 and bitmap[y+1][x]:
#         y = y+1
#     else:
#         pass

#     print(bitmap[y][x])
#     my_dice[com] = bitmap[y][x]


#     return x, y

import sys

# 주사위 굴리는 함수 정의
def rolling(dice, i, x_pos, y_pos, com):
    if i == 1 and x_pos < M-1:
        x_pos += 1
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]
    elif i == 2 and x_pos > 0:
        x_pos -= 1
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]
    elif i == 3 and y_pos > 0:
        y_pos -= 1
        dice[1], dice[5], dice[6], dice[2], dice[4], dice[3] = dice[5], dice[6], dice[2], dice[3], dice[4], dice[1]
    elif i == 4 and y_pos < N-1:
        y_pos += 1
        dice[1], dice[5], dice[6], dice[2], dice[4], dice[3] = dice[6], dice[5], dice[1], dice[2], dice[4], dice[3]
    else:
        return x_pos, y_pos, com, dice[1]

    return x_pos, y_pos, com, dice[1]

input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())

bitmap = []
for i in range(N):
    bitmap.append(list(map(int, input().split())))

command = list(map(int, input().split()))

# 주사위 초기값 설정
my_dice = [0] * 7
com = 0
for i in command:
    x, y, com, val = rolling(my_dice, i, x, y, com)
    if val:
        print(val)
        my_dice[com] = 0
    else:
        print(0)

