from collections import deque

r, k = map(int, input().split())

graph = [list(input()) for _ in range(R)]
# 좌표 위에 뭔가 있으면 True로 방문 처리
visited = [[False] * C for _ in range(R)]
sec, x,y = map(int, input().split())



for i in range(k):
    virus =[]

virus_1 = deque()  # 고슴도치
virus_2 = deque()  # 물
count = 0  # 시간(초) 카운트

# 방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(r):
    for j in range(r):
        if graph[i][j] == 'D':
            home.append([i,j])
        elif graph[i][j] == '*':
            queue.append([i,j])
        elif graph[i][j] == 'S':
            gosm.append([i,j])
        elif graph[i][j] == 'X':
            rock.append([i,j])
        else:
            continue