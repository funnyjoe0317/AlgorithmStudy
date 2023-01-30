
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
    
visited = [[False] * n for _ in range(n)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0

ans =[]

def bfs(x,y):
    global cnt
    # 큐 구현을 위해 deque라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x +dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 모든 리스트가 TRue였을 때 while문 탈출
            # if all(visited) ==  True:
            #     print(cnt)
            #     break
            if graph[nx][ny] == 0:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    continue
                else:
                    # 1단지를 탐색이 끝난후에는 새로운 0을 큐에 집어넣어 출발가능하게함
                    queue.append((nx, ny))
                    ans.append(cnt)
                    cnt = 0

            if graph[nx][ny] == 1:
                if visited[nx][ny] == False:
                    # 1단지가 방문하지 않았다면 트루로 체크 중복 체크되는것을 방지하게함
                    visited[nx][ny] = True
                    cnt += 1
                    queue.append((nx, ny))
                else:
                    pass



bfs(0,0)