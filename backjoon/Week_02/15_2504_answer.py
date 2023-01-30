bracket = list(input())
stack=[]
answer = 0
tmp =1
# tem의 뜻은 Temporary 일시적인 값

for i in range(len(bracket)):
    
    if bracket[i] == '(':
        stack.append(bracket[i])
        tmp *= 2

    elif bracket[i] == '[':
        stack.append(bracket[i])
        tmp *= 3

    elif bracket[i] == ')':
        if not stack or stack[-1] == '[':
            # 이게 가능한 이유는 밑에서 pop을 통해 항상 리스트의 데이터가 일정하게 유지됬기 때문?
            answer = 0
            break
        if bracket[i-1]=='(':
            answer += tmp
        stack.pop()
        tmp //=2
        # tmp가 곱되어 진것을 다시 초기화
    
    else:
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if bracket[i-1] == '[':
            answer += tmp

        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer) 