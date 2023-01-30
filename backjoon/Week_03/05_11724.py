# 드디어 혼자 풀었다!!!

import sys
from collections import deque
input= sys.stdin.readline

n, d =  map(int, input().split())
graph = [[] for _ in range(n+1)]
count = 0

def bfs(graph, start, visited):
    global count
    queue = deque([start])
    visited[start] = True
    count += 1
    while queue:
        v= queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * (n+1)

for i in range(d):
    point_1, point_2 = map(int, input().split()) 
    if i ==0:
        fir = point_1
    graph[point_1].append(point_2)
    graph[point_2].append(point_1)

for i in range(1, n+1):
    if visited[i] != True:
        bfs(graph, i, visited)

print(count)

