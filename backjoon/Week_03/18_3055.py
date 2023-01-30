import sys
from collections import deque

n, m = map(int, input().split())  # mn크기, 맵 정보
graph = [list(input().strip()) for _ in range(n)]

gosm=deque([])
water=[]
rock=[]
home = []
queue = deque([])
print(graph)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 물, 집, 돌 위치 정보 받기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'D':
            home.append([i,j])
        elif graph[i][j] == '*':
            queue.append([i,j])
        elif graph[i][j] == 'S':
            gosm.append([i,j])
        elif graph[i][j] == 'X':
            rock.append([i,j])
        else:
            continue
        
print(home)
def bfs(x,y):
    # 큐 구현을 위해 deque라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복하기
    # 시작 지점 잡아 주어야한다 받을 때
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x +dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 돌과 햄스터 집인 경우 무시
            if graph[nx][ny] == 'X' or 'D':
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                # 그래프 현재 위치의 값을 1 더해준다. 1->2->3
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

    # 2차원 리스트의 맵 정보 입력 받기

# for i in range(m):
#     tmp = []
#     # 리스트 수만큼 받아주고
#     tmp.append(list(map(str, input())))
#     for j in range(n):
#         # 이제 시작지점, 돌, 집을 찾아주자
#         if tmp[j] == '*':
#             queue.append([i, j])
#     graph.append(list(map(int, input())))

# print(queue)
# print(graph)

# # for i in range(h):
#     tmp = []
#     for j in range(n):
#         tmp.append(list(map(int, sys.stdin.readline().split())))
#         for k in range(m):
#             if tmp[j][k] == 1:
#                 queue.append([i, j, k])
#     graph.append(tmp)

