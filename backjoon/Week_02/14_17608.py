import sys
input = sys.stdin.readline

N = int(input())

stack = []
count = 1
for i in range(N):
    stack.append(int(input()))

last = stack[-1]

for i in reversed(range(N)):
    if last < stack[i]:
        count += 1
        last = stack[i]

print(count)

