from collections import deque
import queue

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
# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
    # 큐에서 하나의 원소를 뽑아 출력하기
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * 9
bfs(graph, 1, visited)


# def dfs(graph, v, visited):
#     # 매개변수 그래프에대한 정보, 시작시점, 방문 했는지
#     # 현재 노드를 방문 처리
#     visited[v] = True
#     # 해당노드를 방문처리 한다. 처음 1이 false에서 true로 바뀜
#     print(v, end=' ')
#     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
    
# #   각 노드가 방문된 정보를 표현(1차원리스트)
# visited = [False] * 9
# # 정의된 DFS 함수 호출
# dfs(graph, 1, visited)



# 재귀를 이용한 DFS구현 (오른쪽 자식노드가 이상하게 진행이 안됨)

# def recursive_dfs(v, discovered=[]):
#     discovered.append(v)
#     for w in graph[v]:
#         if w not in discovered:
#             discovered = recursive_dfs(w, discovered)
#         return discovered

# print(recursive_dfs(1))


# # DFS 스택을 이용한 반복 구조로 구현

# def iterative_dfs(start_v):
#     discovered =[]
#     stack =[start_v]
#     while stack:
#         v = stack.pop()
#         if v not in discovered:
#             discovered.append(v)
#             for w in graph[v]:
#                 stack.append(w)
#     return discovered


# print(iterative_dfs(1))

# def iterative_bfs