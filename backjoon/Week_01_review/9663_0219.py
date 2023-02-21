# 9663 N-Queen
import sys
input = sys.stdin.readline

N = int(input())
pos = [0] * N                       # 각 열에 배치한 퀸의 위치

flag_a = [False] * N                # 각 행에 퀸을 배치했는지 체크
flag_b = [False] * (N*2-1)          # 대각선 방향으로 퀸을 배치했는지 체크
flag_c = [False] * (N*2-1)          # ``

answer = []

cnt = 0
def put() -> None:
    # 각 열에 배치한 퀸의 위치를 출력
    # for i in range(N):
    #     print(f'{pos[i]:2}', end='')
    # print()
    global cnt
    cnt += 1

def set(i: int) -> None:
    # i열에 알맞은 위치에 퀸을 배치
    for j in range(N):
        if( not flag_a[j] and not flag_b[i+j] and not flag_c[i - j +(N-1)]):
            pos[i] = j
            if i ==N-1:
                put()
            else:
                flag_a[j] = flag_b[i +j] = flag_c[i - j +(N-1)] = True
                set(i +1)
                flag_a[j] = flag_b[i+j] = flag_c[i - j +(N-1)] = False

set(0)
print(cnt)
