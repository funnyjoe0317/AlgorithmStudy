import sys
import itertools
nCr = itertools.combinations
input = sys.stdin.readline

# {1,...,49} 중 6개 선택 - nCr
# 전략 k 개 6보다큼 고른수 S 그 수만가지고 번호 선택
# k 7~12
# 0 입력될뗴 까지 반복
count = 1
while True:
    case = list(map(int, input().split()))
    if case[0] == 0:
        break
    else:
        # 얘도 왜?
        case = case[1:]
        groups = list(nCr(case, 6))
        for group in groups:
            group = map(str, group)
            print(' '.join(group))