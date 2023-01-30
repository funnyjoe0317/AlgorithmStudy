# 1. 출발 노드를 설정합니다.
# 2. 최단 거리 테이블을 초기화합니다. 자기자신= 0
# 3. 반복 방문하지 않은 노드중에서 최단거리가 가장 짧은 노드를 선택합니다. 그리디 알고리즘
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단거리 테이블을 갱신합니다.
# 5. 위 과정에서 3번과 4번을 반복합니다. 

# 알고리즘 동작 과정에서 최단 거리 테이블을 각 노드에 대한 현재까지의 최단거리 정보를  가지고있습니다.
# 처리 과정에서 더 짧은 경로를 찾으면 '이제부터는 이경로가 제일 짧은 경로'라고 갱신합니다.

import sys
import heapq
input = sys.stdin.readline
INF = int(1E9)
# 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수
n,m = map(int,input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있느닞 체크하는 목적의 리스트를 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선의 정보를 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용 c
    graph[a].append((b,c))

def get_smallest_node():
    min_value = INF
    index = 0
    # 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
        # 시작노드를 제외한 전체 n-1 개의 노드에 대해 반복
    for i in range(n -1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    # 최대힙 사용시 -value
    for i in range(len(h)):
        result.append(heapq.heappop(h))
        # -heapq 해야댐
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

dijkstra(start)

# 모든 노드로 가기위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(infinity)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


# 다익스트라 알고리즘 : 개선된  구현방법
# 단계마다 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드를 선택하기 위해 힙