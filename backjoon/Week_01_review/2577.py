# 숫자의 개수

# 1. 숫자 3개를 입력받는다.
# 2. 각 숫자를 곱한 결과를 구한다.
# 3. 각 숫자의 개수를 구한다.

number_list = []

for i in range(3):
    num = int(input())
    number_list.append(num)

result = number_list[0] * number_list[1] * number_list[2]

result_list = list(map(int, str(result)))
for j in range(10):
    print(result_list.count(j))

# count 함수는 문자열 내부에서 특정 문자, 혹은 문자열이 포함 되어있는지 계산해서 반환해주는 함수 입니다

# 0208
