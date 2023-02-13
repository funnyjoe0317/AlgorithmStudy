# 1303 전쟁
import sys
from collections import deque
# deque 라이브러리 사용
input = sys.stdin.readline
 
def bfs(x, y, color):
    cnt = 0
    queue = deque()
    # 큐 구현을 위해 deque 라이브러리 사용
    queue.append((x, y))
    visited[x][y] = True
 
    while queue:
        x, y = queue.popleft()
 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
 
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == color and not visited[nx][ny]:
                    # if color is same and not visited
                    # append queue and visited
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    cnt += 1    # each color count
 
    return cnt + 1
 
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
graph = [list(input()) for _ in range(m)]
visited = [[False] * n for i in range(m)]
 
white, blue = 0, 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W' and not visited[i][j]:
            white += bfs(i, j, 'W') ** 2    # count accumulate
        elif graph[i][j] == 'B' and not visited[i][j] :
            blue += bfs(i, j, 'B') ** 2    # count accumulate
 
print(white, blue)





# import sys
# import collections
# input = sys.stdin.readline

# N, M = map(int, input().split())
# field = []
# for i in range(M):
#     field.append(list(input().rstrip()))

# color = ['W', 'B']
# graph = {'W': [], 'B': []}

# def bfs(field, i, j, color):
#     queue = collections.deque()
#     # collection.deque()는 list와 비슷하지만, list보다 빠르다.
#     # list는 삽입, 삭제가 느리지만, deque는 삽입, 삭제가 빠르다.
#     # list는 인덱싱이 빠르지만, deque는 인덱싱이 느리다.
#     # list는 중간에 삽입, 삭제가 느리지만, deque는 중간에 삽입, 삭제가 빠르다.
#     # deque는 스택, 큐의 기능을 모두 지원한다.
#     queue.append((i, j))
#     count = 0
#     while queue:
#         i, j = queue.popleft()
#         graph[color].append((i, j))
#         if i < 0 or i >= len(field) or j < 0 or j >= len(field[0]):
#             continue
#         if graph[i][j] == 'B' or graph[i][j] == 'W':
#             continue
#         if field[i][j] == color:
#             # field[i][j] = 'B'
#             count += 1
#             queue.append((i+1, j))
#             queue.append((i-1, j))
#             queue.append((i, j+1))
#             queue.append((i, j-1))
#     return count**2
# white = 0
# blue = 0
# for i in range(M):
#     for j in range(N):
#         if field[i][j] == 'W':
#             white += bfs(field, i, j, 'W')
#         elif field[i][j] == 'B':
#             blue += bfs(field, i, j, 'B')

# print(white, blue)


# field = []

# for i in range(M):
#     field.append(list(input().rstrip()))

# def dfs(field, i, j, color):
#     # 만약에 적군이거나 필드에서 나간 경우
#     if i < 0 or i >= len(field) or j < 0 or j >= len(field[0]):
#         return
    
#     if field[i][j] == 'B' or field[i][j] == 'W':
#         return

#     field[i][j] = color

    
#     # if field[i][j] == color:
#     #     return
    
#     dfs(field, i+1, j, color)
#     dfs(field, i-1, j, color)
#     dfs(field, i, j+1, color)
#     dfs(field, i, j-1, color)


# for i in range(M):
#     for j in range(N):
#         if field[i][j] == 'W':
#             dfs(field, i, j, 'W')
#         elif field[i][j] == 'B':
#             dfs(field, i, j, 'B')


# print(field)


# 1. dfs로 적군을 찾는다.
# 2. 찾은 적군을 0으로 바꾼다.
# 3. 0이 아닌 적군을 찾는다.
# 4. 0이 아닌 적군을 찾으면 다시 dfs를 돌린다.
# 5. 0이 아닌 적군을 찾을 때까지 반복한다.