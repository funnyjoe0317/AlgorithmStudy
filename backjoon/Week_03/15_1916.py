import sys
import heapq
from sys import maxsize

input=sys.stdin.readline
n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [maxsize] * (n + 1)
heap = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

start, end = map(int, input().split())

def dijkstra(x):
    pq = []
    heapq.heappush(pq, (0, x))
    visited[x] = 0

    while pq:
        d, x = heapq.heappop(pq)

        if visited[x] < d:
            continue

        for dis, point in graph[x]:
            nd = d + dis

            if visited[point] > nd:
                heapq.heappush(pq, (nd, point))
                visited[point] = nd

dijkstra(start)

print(visited[end])


        # d가 그래프에서 1이 다돌면 새로 갱신되어서 
        # 새로운 위치에서 시작할 수 있게 한다.