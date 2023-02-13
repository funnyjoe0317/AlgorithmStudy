# 2750 수 정렬하기

import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

sorted_arr = sorted(arr)

for i in range(n):
    print(sorted_arr[i])