# 2798 분해합
import sys
input= sys.stdin.readline
# 순열, 조합 라이브러리 사용
from itertools import combinations

# 문제는 들어오는 숫자들 중에 합이 Num_sum과 같은 값을 찾으면 된다.

# N 들어오는 숫자의 개수
N, Num_sum = map(int, input().split())


min_gap = 1000000000000

# 숫자들을 리스트화
N_list = list(map(int, input().split()))
# print(N_list)

# print(list(combinations(N_list,3)))
data = list(combinations(N_list,3))

# 3개 조합의 합으로 차이를 계산해서 차이가 더 작은게 들어오면 정답을 교체하는 식으로 하고자 한다. 
for i in range(len(data)):
    gap = sum(data[i])
    # print(gap)
    if gap <= Num_sum and min_gap >= Num_sum - gap:
        min_gap = Num_sum - gap
        ans = gap

print(ans)