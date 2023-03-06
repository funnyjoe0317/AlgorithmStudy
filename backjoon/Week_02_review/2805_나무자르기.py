# 2805_나무자르기기
import sys
input = sys.stdin.readline

N, H = map(int, input().split())

Tree =  [int(x) for x in input().split()]

Tree.sort()

def two_minSerch(lst, target):
    left = lst[0]
    # -1 은 맨 뒤에 있는 데이터
    right = lst[-1]
    while left <= right:
        mid = (left + right) // 2
        answer = sum([i-mid for i in lst if i>mid])
        # for i in lst:
        #     if i > mid:
        #         answer += i - mid
        if answer == target:
            return mid
        elif answer >target:
            left = mid+1
        elif answer < target:
            right = mid-1

print(two_minSerch(Tree, H))

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

left, right = 0, max(trees) # 나무 높이의 최댓값으로 초기화

while left <= right:
    mid = (left + right) // 2 # 이분 탐색으로 찾을 높이
    cut = sum(tree - mid for tree in trees if tree > mid) # 높이가 mid일 때 절단기로 잘라서 가져갈 수 있는 나무 길이
    if cut >= M:
        left = mid + 1 # 높이를 높여서 가져갈 수 있는 나무 길이를 줄임
        answer = mid
    else:
        right = mid - 1 # 높이를 낮춰서 가져갈 수 있는 나무 길이를 늘임

print(answer)

        
    