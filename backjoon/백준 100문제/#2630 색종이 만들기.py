# 색종이 만들기

import sys
sys.setrecursionlimit(10**6)

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

blue = 0
white = 0

def check(x, y, n):
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                check(x, y, n//2)
                check(x, y+n//2, n//2)
                check(x+n//2, y, n//2)
                check(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        white[0] += 1
    else:
        blue[0] += 1
check(0, 0, N)
print(white)
print(blue)

