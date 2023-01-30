import sys

N = int(sys.stdin.readline())

stack = []

result = 0

for i in range(N):
    number = int(sys.stdin.readline())
    if number == 0:
        if len(stack)== 0:
            pass
        else:
            del stack[len(stack)-1]
    else:
        stack.append(number)

if stack==[]:
    print('0')
else:
    sum_list = sum(stack)
    print(sum_list)
