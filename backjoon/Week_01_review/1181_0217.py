# 단어 정렬

import sys
input = sys.stdin.readline
arr = []
N = int(input())
for i in range(N):
    tmp = str(input())
    arr.append(tmp)

arr = list(set(arr))
sorted_words = sorted(arr, key=lambda x: (len(x), x))

for i in range(len(sorted_words)):
    print(sorted_words[i], end='')