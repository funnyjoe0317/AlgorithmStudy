# 외판원 순회 10971

import sys
import itertools
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

INF = sys.maxsize

def tsp(n, graph):
    min_dist = INF
    for path in itertools.permutations(range(1, n)):
        prev = 0
        dist = 0
        for cur in path:
            dist += graph[prev][cur]
            prev = cur
        dist += graph[prev][0]
        min_dist = min(min_dist, dist)
    return min_dist

print(tsp(N, graph))
