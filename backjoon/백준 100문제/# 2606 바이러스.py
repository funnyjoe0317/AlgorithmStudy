# 바이러스
# BFS
# BFS는 너비 우선 탐색이라고도 하며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘입니다.
# BFS는 큐 자료구조를 이용하며, 구체적인 동작 과정은 다음과 같습니다.
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 합니다.
# 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리합니다.
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.
#
# DFS는 깊이 우선 탐색이라고도 하며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘입니다.
# DFS는 스택 자료구조(혹은 재귀 함수)를 이용하며, 구체적인 동작 과정은 다음과 같습니다.
# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 합니다.
# 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면, 그 인접 노드를 스택에 넣고 방문 처리합니다.
# 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냅니다.
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.W
#
# BFS는 DFS보다 더 빠르게 동작합니다.
# BFS는 최단 경로를 찾는 알고리즘으로도 활용됩니다.
# BFS는 큐 자료구조를 이용하며, 구체적인 동작 과정은 다음과 같습니다.


import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
# 미리 그래프를 만들어 놓는다.
# 그래프는 2차원 리스트로 표현할 수 있다.

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start, visited):
    queue = [start]
    # 큐 구현을 위해 deque 라이브러리 사용
    visited[start] = True
    # 현재 노드를 방문 처리
    while queue:
        v = queue.pop(0)
        # 큐에서 하나의 원소를 뽑아 출력
        for i in graph[v]:
            # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
            if not visited[i]:
                # 방문하지 않은 노드라면
                queue.append(i)
                # 큐에 삽입
                visited[i] = True
    return visited


visited = [False] * (N+1)
# 각 노드가 방문된 정보를 리스트 자료형으로 표현
bfs(graph, 1, visited)
print(sum(visited)-1)
# 정의된 BFS 함수 호출



