# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문

def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or  y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문처리
        graph[x][y] = 1
        # 상,하,좌,우의 위치들도 모두 재귀적으로 호출
        # 재귀적 호출의 이유 주변값들을 전부 1로 바꿔주고,
        # 추후에 return 값을 false로 반환하여 result값이 변하지 않게 하기 위해서
        dfs(x -1, y )
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

graph=[]
# n은 세로 길이, m 은 가로길이
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드에 대하여 음료수 채우기 
result = 0
for i in range(n):
    for  j in range(m):
        if dfs(i,j) == True:
            result += 1
            # 현재 위치에서 DFS수행
print(result)