import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
# 수 대입받기
number = list(map(int, input().split()))
# 연산자 개수 계산
add, sub, mul, div = map(int, input().split())


# 최댓값과 최솟값 초기화
max_value = -1e9
min_value = 1e9

def dfs(i, arr):
    global add, sub, mul, div, max_value, min_value
    # 주어진 수열을 다 받았을 경우 최댓값과 최솟값 계산
    if i == n:
        max_value = max(max_value, arr)
        min_value = min(min_value, arr)
    else:
        if  add > 0:
            add -= 1 
            dfs(i+1, arr + number[i])
            add += 1
        # 빼기
        if sub > 0:
            sub -= 1
            dfs(i+1, arr - number[i])
            sub +=1
        if mul > 0 :
            mul -= 1
            dfs(i+1, arr * number[i])
            mul += 1
        if div >0:
            div -= 1
            dfs(i+1, int(arr/ number[i]))
            div += 1 

dfs(1, number[0])

print(max_value)
print(min_value)