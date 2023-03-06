# 제로

import sys
input = sys.stdin.readline

N = int(input())
stack = []

for i in range(N):
    command = int(input())
    if command == 0:
        stack.pop()
    else:
        stack.append(command)

print(sum(stack))