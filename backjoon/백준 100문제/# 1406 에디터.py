# 1406 에디터
# 한 줄로 된 간단한 에디터를 구현하려고 한다. 이 편집기는 영어 소문자만을 기록
# 최대 600,000글자까지 입력
# 커서가 존재하며 문장의 맨 앞 문장의 맨 뒤 중간 임의의 곳 위치 즉 길이가 L인
# 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우
# L 왼쪽으로 한 칸 옮김, D 오른쪽, B 왼쪽에 삭제, P cnrk

# import sys
# input= sys.stdin.readline


# Do_list = list(map(str, input().rstrip("\n")))
# N = int(input())
# cursor = len(Do_list)

# for _ in range(N):
#     action = list(map(str, input().split()))
#     print(action)
#     if action[0] == "P":
#         Do_list.insert(cursor, action[1])
#         cursor += 1
#     elif action[0] == "L":
#         if cursor > 0:
#             cursor -= 1
#     elif action[0] == "B":
#         if cursor > 0:
#             Do_list.remove(Do_list[cursor-1])
#     else:
#         if cursor < len(Do_list):
#             cursor += 1

# print("".join(Do_list))

# import sys

# text = list(input())
# n = int(input())
# cursor = len(text)

# for i in range(n):
#     command = sys.stdin.readline().split()

#     if command[0] == "L" and cursor > 0:
#         cursor -= 1
#     elif command[0] == "D" and cursor < len(text):
#         cursor += 1
#     elif command[0] == "B" and cursor > 0:
#         text.pop(cursor-1)
#         cursor -= 1
#     elif command[0] == "P":
#         text.insert(cursor, command[1])
#         cursor += 1

# for i in range(len(text)):
#     print(text[i], end="")

#------------- 이해 한번 하기 ---------------
import sys

# 기존 스택을 저장하기 위해서 만든 리스트
stack_old = list(input())
# 새로운 스택을 만드는데 이유는 스택 올드앤 뉴로 커서의 이동 역시 포함할 수 있기 때문에
stack_new = []
# for문을 위해서
n = int(input())

for i in range(n):
    # 커맨드 파싱
    command = sys.stdin.readline().split()

    # 문자열 L 이고 stack_old에 원소가 있을 때 True
    if command[0] == "L" and stack_old:
        # stack_old에 마지막 원소를 꺼내어 stack_new에 삽입
        stack_new.append(stack_old.pop())
    # 문자열 D 이고 stack_new에 원소가 있을 때 True
    elif command[0] == "D" and stack_new:
        # D는 오른쪽으로 커서를 옮기는 것이기에 stack_new에 있는것을 왼쪽으로
        stack_old.append(stack_new.pop())
    # 문자열 B 이고 stack_new에 원소가 있을 때 True
    elif command[0] == "B" and stack_old:
        # 삭제하는것 이기에 팝만 하면된다.
        stack_old.pop()
    # 문자열 P 일 때
    elif command[0] == "P":
        # 스택 올드에 문자 추가, 스택 올드는 현재 커서의 위치를 포함한다.
        stack_old.append(command[1])

print("".join(stack_old + list(reversed(stack_new))))


#------------- 이해 한번 하기 ---------------

# def editor(action):
#     global cnt
#     global cursor
#     if cnt == 0:
#         cursor = len(Do_list)

#     if action[0] == "P":
#         Do_list.insert(cursor, action[1])
#         cursor += 1
#         cnt += 1
#     elif action[0] == "L":
#         if cursor > 0:
#             cursor -= 1
#             cnt += 1
#     elif action[0] == "B":
#         if cursor > 0:
#             Do_list.remove(Do_list[cursor-1])
#             cnt += 1
#     else:
#         if cursor < len(Do_list):
#             cursor += 1
#             cnt += 1



# for i in range(N):
#     action = list(map(str, input().split()))
#     editor(action)



# import sys

# st1 = list(sys.stdin.readline().rstrip())
# st2 = []

# for _ in range(int(sys.stdin.readline())):
# 	command = list(sys.stdin.readline().split())
#     if command[0] == 'L':
# 		if st1:
#         	st2.append(st1.pop())
            
# 	elif command[0] == 'D':
#     	if st2:
#         	st1.append(st2.pop())

# 	elif command[0] == 'B':
#     	if st1:
#         	st1.pop()
            
# 	else:
#     	st1.append(command[1])
        
# st1.extend(reversed(st2))
# print(''.join(st1))
