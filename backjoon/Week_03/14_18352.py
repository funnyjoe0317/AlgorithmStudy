from collections import deque
import queue

n , k, d, s = map(int, input().split())

# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * (n+1)

graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)

for i in range(n):
    point_1, point_2 = map(int, input().split()) 
    graph[point_1].append(point_2)
    graph[point_2].append(point_1)
    
# print(graph)

def bfs(graph, start, visited):
    answer = []
    queue = deque([start])
    visited[start] = True
    distance[start] = 0

    while queue:
        v= queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
                
                distance[i] = distance[v] + 1
                # 새롭게 True가 나오는 시점에 +1을 하는것이므로 새로운 곳이 나온다면
                # 당연히 있다는 것을 뜻하는데 근대 여러버 나눠져 있으면

                if distance[i] == d:
                    answer.append(i)

    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')

    
bfs(graph, s, visited)