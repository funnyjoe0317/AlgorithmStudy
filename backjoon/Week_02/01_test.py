# 흑백영상 압축하는 데이터 구조 쿼드트리 0과 1로만 ㄴ나타냄

import sys

N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 



def solution(x, y, N) :
  color = data[x][y]
  for i in range(x, x+N) :
    for j in range(y, y+N) :
      if color != data[i][j] :
        solution(x, y, N//2)
        solution(x, y+N//2, N//2)
        solution(x+N//2, y, N//2)
        solution(x+N//2, y+N//2, N//2)
        return
  if color == 0 :
    # 0으로 

  else :



solution(0,0,N)
