# 세준이가 양수와 +- 그리고 ()러 식을 만들었는데, 괄호만 지운거야  왜 그랬을까 이색기는
# 그래서 다시 괄호를 쳐서 최솟값으로 만들려고 하는데 그걸 해달라는거지
# 조건은 0~9, +- 만으로 이루어져있고, 처음과 마지막은 숫자야 연속해서 2개이상의 연산자가 나타나지 않고,

# 5자리보다 많이 연속되는 숫자는 없다 555555 이런거
# 수는 0 으로 시작이 가능해 0 , 10 , 22
# 입력 식의 길이는 50 보다 작거나 같다
# 55-50+40 -> 55 - ( 50 + 40 )
# 처음에 
import sys

input = sys.stdin.readline

expression = list(input().rstrip().split('-'))
# 55+35-25+95
su_m = 0

for i in expression[0].split('+'):
    # 55+35로 나누어 진다
    su_m +=  int(i)
    # 그 후에 for문을 통해서 앞에있는 숫자들을 순서로 더해 준다.
for i in expression[1:]:
    # 처음에 -로 수식을 나누어 줬으므로 나중에 -뒤로의 수식을 1: 슬라이싱으로 나누어주고
    # 마이너스 뒤로는 전부다 나눠주어야해서
    for j in i.split('+'):
        su_m -= int(j)

print(su_m)

# for i in range(len(expression)):
#     if expression[i] == "-":

