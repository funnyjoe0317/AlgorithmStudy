# 달팽이는 올라가고 싶다
import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

#------------부루트 포스 풀이----------------
# cnt = 0
# run = 0

# while run < V:
#     cnt += 1
#     run += A
#     if run >= V:
#         break
#     run -= B

# print(cnt)
#------------부루트 포스 풀이----------------

#------------수학적 풀이----------------

V - A = (A-B) * n
n = (V-A) / (A-B)
n = (V-A) // (A-B)

if (V-A) % (A-B) == 0:
    print(n+1)
else:
    print(n+2)


