
# # input 입력 받기
# n = int(input())
# solution = list(map(int, input().split(' ')))

# # 정렬하기
# solution.sort()

# # 이중포인터 설정
# left = 0
# right = n-1

# answer = abs(solution[left] + solution[right]) # 기준값
# final = [] # 정답

# # 투포인터 진행
# while left < right:
#     s_left = solution[left]
#     s_right = solution[right]

#     tot = s_left + s_right
#     # 두 용액의 합이 0과 가장 가까운 용액을 정답에 담아주기
#     if abs(tot) < answer:
#         answer = abs(tot)
#         final = [s_left, s_right]
	
#     # 두 용액의합이 0보다 작다면 왼쪽의 값을 늘려 조금 더 0에 가깝게 만들어준다
#     if tot < 0:
#         left += 1
#     # 반대로, 두 용액의 합이 0보다 크다면 오른쪽의 값을 줄여서 조금 더 0에 가깝게 만들어준다
#     else:
#         right -= 1

# print(final[0], final[1])

# n = int(input())
# arr = list(map(int, input().split(' ')))
# arr.sort()

# left = 0
# right = n-1

# answer = abs(arr[left] + arr[right])
# final = [arr[left], arr[right]]


# while left < right:
#     left_val = arr[left]
#     right_val = arr[right]

#     sum = left_val + right_val
  
#     if abs(sum) < answer:
#         answer = abs(sum)
#         final = [left_val, right_val]
#         if answer == 0:
#           break
#     if sum < 0:
#         left += 1
#     else:
#         right -= 1

# print(final[0], final[1])
import sys
input = sys.stdin.readline
N = int(input())
sum_li = list(map(int, input().split(' ')))
sum_li.sort()

left = 0
right = N-1

answer = abs(sum_li[left]+sum_li[right])
# 지금의 기준점으로 첫값과 끝같의 합을 잡아 놓고 나중에 더 작은 합이 나온다면
# answer 값을 바꿔주면 된다.
final = [sum_li[left], sum_li[right]]
# 마지막 리스트 왼쪽 오른쪽을 따로 저장하여 출력하기 위해서

while left < right:
    left_val = sum_li[left]
    right_val = sum_li[right]
    sum = left_val + right_val

    if abs(sum) < answer:
        answer = abs(sum)
        final = [left_val, right_val]
        if answer == 0:
            break
    if sum < 0:
        left += 1
    else:
        right -= 1

print(final[0], final[1])

