import sys
from collections import deque


num, member = map(int, sys.stdin.readline().split())
arr = []
graph = [[] for _ in range(member+1)]
inDegree = [0 for _ in range(member+1)]
queue = deque()
answer = []

for i in range(member):
    height_1, height_2 = map(int, input().split())
    answer.append([height_1, height_2])

for height_1, height_2 in answer:
    inDegree[height_2] += 1
    graph[height_1].append(height_2)

for i in range(1, num+1):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    student = queue.popleft()
    # indegree가 0인 정점을 제거하고, 해당 정점이 참조하고 있던 점들의
    # indegree를 감소시킨다.
    for i in graph[student]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            queue.append(i)
    print(student, end = ' ')