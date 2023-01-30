import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, str(input().rstrip())))for _ in range(n)]
dx = (1, -1, 0, 0,)
dy = (0, 0, 1, -1)


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    matrix[x][y] = 0
    cnt = 1
    while queue:
        now_c, now_r = queue.popleft()
        for i in range(4):
            next_c = now_c + dy[i]
            next_r = now_r + dx[i]

            if 0 <= next_c < n and 0 <= next_r < n:
                if matrix[next_c][next_r] == 1:
                    matrix[next_c][next_r] = 0
                    queue.append((next_c, next_r))
                    cnt += 1
    return cnt


ans = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            ans.append(bfs(i, j))

ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])