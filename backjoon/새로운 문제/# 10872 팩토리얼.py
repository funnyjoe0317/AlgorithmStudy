# 팩토리얼
import sys
input= sys.stdin.readline

N = int(input())

def factorial(N):
    if N == 0:
        return 1
    else:
        return N * factorial(N-1)

print(factorial(N))