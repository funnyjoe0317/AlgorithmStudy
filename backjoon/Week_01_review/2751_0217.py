# 수 정렬하기3 0217

import sys
input = sys.stdin.readline
N = int(input())
arr = [0]*10001
# arr = [0]*10000001

for i in range(N):
    arr[int(input())] += 1
    # arr 안에 입력받은 수를 인덱스로 하여 +1씩 해준다.
for i in range(10001):
    if arr[i] != 0:
        # arr[i]가 0이 아니면
        for j in range(arr[i]):
            print(i)