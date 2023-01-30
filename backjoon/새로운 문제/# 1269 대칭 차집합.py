# 1269 대칭 차집합

import sys
input= sys.stdin.readline

N = map(int, input().split())

num_list_1 = set(map(int, input().split()))
num_list_2 = set(map(int, input().split()))

diff_1 = num_list_1.difference(num_list_2)
diff_2 = num_list_2.difference(num_list_1)

print(len(diff_1) + len(diff_2))