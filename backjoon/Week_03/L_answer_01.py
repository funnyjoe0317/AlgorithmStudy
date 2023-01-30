
# 맞왜틀 흑흑흑
import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, k = map(int, input().split())
time_limit, col, row = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)


def bfs():
    queue = deque()

    for num in range(1, k+1):
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == num:
                    queue.append((i, j, 0))
    # 1부터 k까지 순서대로 쭉 넣는다 그러면 1부터 순서대로 점령하겄지..
    while queue:
        now_c, now_r, sec = queue.popleft()
        if sec == time_limit:
            break
            # 일단 현재 바이러스의 좌표
        for i in range(4):
            next_c = now_c + dy[i]
            next_r = now_r + dx[i]
        # 상하좌우를 돌자
            if 0 <= next_c < n and 0 <= next_r < n:
                # 일단 판때기를 벗어나지 않는 선에서
                if matrix[next_c][next_r] == 0:
                    matrix[next_c][next_r] = matrix[now_c][now_r]
                    queue.append((next_c, next_r, sec+1))
                # 상화좌우를 돌면서 0이면 점령이 가능하다.


bfs()
print(matrix[col-1][row-1])