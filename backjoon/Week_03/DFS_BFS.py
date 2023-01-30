
def dfs(graph, v, visited):
    # 현재 노드를 방문처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 연결된 정보를 표현(2차원 리스트)
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
dfs(graph, 1, visited)


 
