from collections import deque
# 넓은 판에 큐로 생각을 해야 풀린다
# 하나하나씩 더해 지기 때문에 좌표값에 들어오는 
# 데이터는 무조건 최소값이다.

# def bfs(x,y,z):
#     # 큐 구현을 위해 deque라이브러리 사용
#     queue = deque()
#     queue.append((x,y,z))
#     # 큐가 빌 때까지 반복하기
#     while queue:
#         x, y = queue.popleft()
#         # 현재 위치에서 4가지 방향으로의 위치 확인
#         for i in range(6):
#             nx = x +dx[i]
#             ny = y + dy[i]
#             nz = z + dz[i]
#             # 미로 찾기 공간을 벗어난 경우 무시
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             # 벽인 경우 무시
#             if graph[nx][ny] == -1:
#                 continue
#             # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 # 그래프 현재 위치의 값을 1 더해준다. 1->2->3
#                 queue.append((nx, ny))
#     # 가장 오른쪽 아래까지의 최단 거리 반환
#     return graph[n-1][m-1]

# N, M 을 공백을 기준으로 구분하여 입력받기
x , y, z= map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []

for i in range(z-1):
    for j in range(y-1):
        graph.append(list(map(int, input())))

print(graph)

# 이동할 네가지 방향 정의
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]



# print(bfs(0,0,몰로 하지?))