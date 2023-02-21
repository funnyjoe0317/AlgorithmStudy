# 1932 정수 삼각형
import sys
input = sys.stdin.readline
N= int(input())
arr = []
# arr = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
for i in range(N):
    arr.append(list(map(int, input().split())))

dp = {} # 메모제이션을 위한 딕셔너리

# dp 함수 정의
def dp_func(i, j):
    # base case
    if i == len(arr)-1:
        return arr[i][j]
    
    # 이미 계산한 결과가 있다면 바로 반환
    if (i  ,j) in dp:
        return dp[(i,j)]
    
    # 계산한 결과가 없다면
    res = 0
    res = max(res, dp_func(i+1,j) + arr[i][j])
    res = max(res, dp_func(i+1,j+1) + arr[i][j])
    dp[(i,j)] = res

    return  res

# 최대 합 구하기
max_sum = dp_func(0,0)
print(max_sum)

