import sys
import heapq

input = sys.stdin.readline

n = int(input())
maze = []
for _ in range(n):
    maze.append(list(map(int, input().rstrip())))

# 2차원 리스트에서 상하좌우 이동을 위한 dirction x, direction y 변수 선언
dx = [1, -1 ,0, 0]
dy = [0, 0, 1, -1]

# 방문 여부 체크를 위한 visited 2차원 리스트
visited = [[False] * n for _ in range(n)]

def bfs(x, y):
    heap = []
    heapq.heappush(heap, (0, x, y))

    while heap:
        count, cx, cy = heapq.heappop(heap)
        visited[cx][cy] = True

        # 도착지점에 도착했을 경우
        if cx == (n - 1) and cy == (n - 1):
            return count

        # 상하좌우로 한칸씩 이동하여 탐색 진행
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if (0 <= nx < n) and (0 <= ny < n) and not visited[nx][ny]:
                # 방문처리
                visited[nx][ny] = True
                # 흰 방
                if maze[nx][ny] == 1:
                    heapq.heappush(heap, (count, nx, ny))
                # 검은 방
                else:
                    heapq.heappush(heap, (count + 1, nx, ny))

print(bfs(0, 0))