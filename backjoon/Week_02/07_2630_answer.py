import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 0과 1로만 나타냄 

blue = 0
white =0

def solution(x,y,N): # x,y 좌표, N: 한변의 길이
    global white,blue # 전역변수 사용
    color = board[x][y] # 첫번째 색깔
    for i in range(x, x+N): # 한변의 길이만큼 반복
        for j in range(y,y+N): # 한변의 길이만큼 반복
            if color != board[i][j]: # 색깔이 다르면
                solution(x,y,N//2) # 4분할
                solution(x,y+N//2,N//2) # 4분할
                solution(x+N//2,y,N//2)
                solution(x+N//2,y+N//2,N//2)
                return
    if color == 0:
        white +=1
    else:
        blue +=1

solution(0,0,N)
print(white)
print(blue)