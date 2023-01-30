from collections import deque
import queue

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v= queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8], 
    # 1에서 접근 할 수 잇는 노드
    [1,7],
    # 2에서 접근 할 수 잇는 노드
    [1,4,5],
    # 3에서 접근 할수 있는 노드
    [3,5],
    # 4에서 접근 가능한
    [3,4],
    # 5에서
    [7],
    # 6에서
    [2,6,8],
    # 7에서
    [1,7]
    # 8에서
]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False]*9

# 정의된 DFS 함수 호출
bfs(graph, 1, visited)