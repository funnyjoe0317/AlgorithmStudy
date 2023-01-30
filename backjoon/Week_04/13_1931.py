# 한개의 회의실이 있느데 n개의 회의에 대하여 회의실 사용표를 만들려고한다.
# 회의가 겹치지 않게 하고 회의실을 사용할수있는 최대 개수
# 회의실을 최대한 사용할 수 있는 코드를 짜라

# 입력값은 미팅 수 와 시작시간과 끝나는 시간이다.

import sys

input = sys.stdin.readline
n = int(input())

room_li = []
for i in range(n):
    room_li.append(list(map(int, input().split())))

room_li.sort(key = lambda x: x[0])
# 일단 시작점을 1에 근접한 값들로 설정을 한다

room_li.sort(key = lambda x: x[1])
# 시작점이 오른 차순을 시작으로 end값에 따라 end값이 기달면 배열을 뒤로
# 밀어 버린다.   이렇게 되면 나중에 end값만 보면 최대 회의의 개수를 알 수 있게된다.

cnt = 1
print(room_li)
end = room_li[0][1]

for i in range(1, n):
    if room_li[i][0] >= end:
        cnt += 1
        end = room_li[i][1]

print(cnt)





n=int(input())
kaigi=[]
kaigi_answer=[]
count=0
for _ in range(n):
    kaigi.append(list(map(int,input().split())))
kaigi.sort()
temp=sorted(kaigi,key=lambda x: x[1])
kaigi=temp
kaigi_answer.append(kaigi[0])
for i in range(1,n):
    j = len(kaigi_answer)
    if kaigi[i][0] >= kaigi_answer[j-1][1]:
        kaigi_answer.append(kaigi[i])
print(len(kaigi_answer))

