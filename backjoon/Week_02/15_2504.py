import sys
input = sys.stdin.readline

stack = []

bracket = list(map(str, sys.stdin.readline()))
Ocount = 0
Lcount =0
point=[]
del bracket[-1]
for i in range(len(bracket)):
    if bracket[i]=='(' :
        Ocount += 1
        if Ocount >=2:
            Omultiply = Ocount
        # 수정 해야 할 부분

    elif bracket[i] == '[':
        Lcount += 1
        if Lcount >=2:
            Lmultiply = Lcount

    elif bracket[i] == ')':
        Ocount -= 1
        if Ocount < 0:
            print('0')
        elif Ocount == 0:
            if Omultiply >=2:
                2**Omultiply
            else:
                point.append(2)

    elif bracket[i] == ']':
        Lcount -= 1
        if Lcount <0:
            print('0')
        elif Lcount ==0:
            if Lmultiply >=2:
                3**Lmultiply
        





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