# import sys

# input= sys.stdin.readline

# # def dfs(graph, v, visited):
# #     # 현재 노드를 방문처리
# #     visited[v] = True

# #     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
# #     for i in graph[v]:
# #         if not visited[i]:
# #             print(graph[i])
# #             dfs(graph, i, visited)

# n = int(input())

# graph = [[] for i in range(n+1)] # 빈 그래프 생성

# visited = [False] * (n+1)

# for i in range(1,n):
#     point_1, point_2 = map(int, input().split()) 
#     graph[point_1].append(point_2)
#     graph[point_2].append(point_1)

# for i in range(2, n+1):
#     print(graph[i][0])

import sys

input= sys.stdin.readline
sys.setrecursionlimit(10**9)

n=int(input())
# 노드의 개수
tree = [[] for _ in range(n+1)]

# 부모노드의 저장
parents = [0 for _ in range(n+1)]

# 트리 구조 입력
for i in range(1,n):
    point_1, point_2 = map(int, input().split()) 
    tree[point_1].append(point_2)
    tree[point_2].append(point_1)

def DFS(s,tree,parents):
    # 연결된 노드들부터 parents[i]의 부모가 없으면 부조 설정 해주고, DFS돌린다.
    for i in tree[s]:
        if parents[i] == 0:
            parents[i] = s
            DFS(i,tree,parents)

DFS(1, tree,parents)

for i in range(2,n+1):
    print(parents[i])