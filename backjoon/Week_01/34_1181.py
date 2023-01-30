# 단어들 중복 제거 그 후 정렬

from unittest import result


n = int(input())
textlist=[]
result=[]

for i in range(n):
    text_t =input()
    textlist.append(text_t)

# 중복값 제거 함수
for value in textlist:
    if value not in result:
        result.append(value)


