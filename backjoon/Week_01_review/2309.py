# 일곱 난쟁이
import sys
import itertools
input = sys.stdin.readline


arr = []
for i in range(9):
    arr.append(int(input()))

for i in itertools.combinations(arr, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
