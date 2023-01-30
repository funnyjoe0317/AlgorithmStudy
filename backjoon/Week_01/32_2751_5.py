# 파이선 내장함수를 이용하여 풀이

import sys
n = int(input())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))
for i in sorted(li):
    print(i)

