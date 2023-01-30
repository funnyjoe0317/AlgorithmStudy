
v,e = map(int, input().split())
# 노드의 개수와 간선의 개수 입력 받기
parent = [0] * (v+1)
# 부모테이블이 들어갈곳 초기화

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(1, v+1):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print()

print('부모테이블',) 

# 경로  압축 기법

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 사이클 판별 알고리즘
# 1. 각 간선을 하나씩 확인하여 두 노드의 루트노드를  확인합니다.
# 1) 루트 노드가 서로 다르다면 두 노드에 대하여 합집합(union)연산을 수행
# 2) 루트 노드가 서로 같다면 사이클이 발생한 것입니다. 
# 2. 그래프에 포합되어 있는 모든 간선에 대하여 1번 과정을 반복