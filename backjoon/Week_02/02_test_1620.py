# import sys

# N = int(sys.stdin.readline())

# stack = []


# for i in range(N):
#     count=0
#     number = list(map(str, sys.stdin.readline()))
#     del number[-1]
#     stack.append(number)
#     for j in range(len(stack[i])):
#         if stack[i][j]=='(':
#             count += 1
#         elif stack[i][j]==')':
#             count -= 1
#             if count < 0:
#                 print('NO')
#                 break
            
#     # if stack[i][0] == ')':
#     #     print('NO')
#     if count == 0:
#         print('YES') 
#     elif count >0:
#         print('NO')

# for i in reversed(range(N)):
from collections import deque
import sys

N = list(sys.stdin.readline().rstrip())
N = deque(N)
print(N)
stack=[]
p_count = 0
a_count = 0
for i in reversed(range(len(N))):
    if N[i]=='P':
        P = N.pop()
        stack.append(P)
        if len(stack) > 1:
            if stack[i-len(N)+1] == 'A':
                p_count += 1

    elif N[i] == 'A':
        A = N.pop()
        stack.append(A)
        if len(stack) > 1:
            if stack[i-len(N)+1] == 'A':
                break
            else:
                a_count += 1
    
if a_count*3 == p_count:
    print('PPAP')
elif (a_count*3)-1 == p_count:
    print('PPAP')
else:
    print('PPAP')
