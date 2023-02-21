import sys
import itertools

INF = sys.maxsize
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]


def tsp(n, graph):
    min_dist = INF
    for path in itertools.permutations(range(1, n)):
        # 0 -> 1 -> 2 -> 3 -> 0
        # 0 -> 1 -> 3 -> 2 -> 0
        prev = 0
        dist = 0
        for cur in path:
            # 0 -> 1
            # 1 -> 2
            dist += graph[prev][cur]
            # 1
            prev = cur
            # 1
        dist += graph[prev][0]
        # 0 -> 1 -> 2 -> 0 마지막 과정
        min_dist = min(min_dist, dist)
        # 비교하여 최소 값을 찾기 위한 과정
    return min_dist

print(tsp(n, graph)) 
