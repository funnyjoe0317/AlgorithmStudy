import sys

N = int(sys.stdin.readline())

stack = []


for i in range(N):
    count=0
    number = list(map(str, sys.stdin.readline()))
    del number[-1]
    stack.append(number)
    for j in range(len(stack[i])):
        if stack[i][j]=='(':
            count += 1
        elif stack[i][j]==')':
            count -= 1
            if count < 0:
                print('NO')
                break
            
    # if stack[i][0] == ')':
    #     print('NO')
    if count == 0:
        print('YES') 
    elif count >0:
        print('NO')


