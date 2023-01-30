# 내 생각에는 DFS나BFS 모두 리스트 형태로만 받을수 있다면 출력이 가능하니 
# 입력값을 리스트에만 잘 append하면 될거같다. 

import sys
from collections import deque

input= sys.stdin.readline

# 내답인데 맞았음 고쳐서
def dfs(graph, v, visited):
    # 현재 노드를 방문처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

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


n, d, v =  map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(d):
    point_1, point_2 = map(int, input().split()) 
    graph[point_1].append(point_2)
    graph[point_2].append(point_1)
    # 서로의 점들을 체크하기 위해서 1,2포인트의 순서를
    # 바꿔 append해주면 모든 점들의 연결 표시됨


for i in range(1,n+1):
    graph[i].sort()
    # 혹시나 점들이 순서대로 연결 안되있을수 잇으니깐 소트

visited = [False] * (n+1)
# 지점들을 체크하기위해서 체크(간곳은 True값으로)
dfs(graph, v, visited)
print()
visited = [False] * (n+1)
bfs(graph, v, visited)