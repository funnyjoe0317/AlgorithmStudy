# 괄호의 값

def solution(s):
    stack = []
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                stack.append(2)
            else:
                return 0
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
                stack.append(3)
            else:
                return 0
    print(stack)
    return 0

s = input()
print(solution(s))


