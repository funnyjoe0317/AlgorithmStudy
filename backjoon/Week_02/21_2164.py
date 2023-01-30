from collections import deque
import sys

input = sys.stdin.readline
Qnumber_li = deque([])

N=int(input())
for i in range(1,N+1):
    Qnumber_li.append(i)

#  첫 숫자를 버린다
# 두번째 숫자를 맨뒤로 보낸다

while True:
    if len(Qnumber_li) > 1:
        Qnumber_li.popleft()
        Qnumber_li.append(Qnumber_li[0])
        Qnumber_li.popleft()
    else:
        print(Qnumber_li[0])
        break





# if len(Qnumber_li) > 3:
#     print(Qnumber_li[len(Qnumber_li)-3])
# elif len(Qnumber_li) == 3:
#     print(Qnumber_li[len(Qnumber_li)-2])
# elif len(Qnumber_li) == 2:
#     print(Qnumber_li[1])
# elif len(Qnumber_li) < 2:
#     print(0)



