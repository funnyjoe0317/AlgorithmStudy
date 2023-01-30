import sys
input = sys.stdin.readline


# n = int(input())
# soo = list(map(int, input().split()))


# # dp = [1] * n


# # compare = 0

# # for i in range(n):
# #     # for j in range(n):
# #     if i ==0:
# #         continue
# #     if soo[i-1] < soo[i]:
# #         if compare != 0:
# #             # 처음이 아닐 때
# #             if soo[i] > compare:
# #                 dp[i] = dp[i-1] + 1
# #                 compare = soo[i]
# #             else:
# #                 dp[i] = dp[i-1]
# #         elif compare == 0:
# #             dp[i] = dp[i-1] + 1
# #             compare = soo[i]
# #     elif soo[i] < compare:
# #         dp[i] = dp[i-1]

# # print((dp[n-1]))

# 31 84 18 62 35 77 23 53 60 94 3 77 60 51 42 18 83 85 63 51

import sys

N = int(sys.stdin.readline())
A = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N) :
    for j in range(i) :
        if A[i] > A[j] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))


# if i == 0 or j == 0:  # 마진 설정
# 	LCS[i][j] = 0
# elif string_A[i] == string_B[j]:
# 	LCS[i][j] = LCS[i - 1][j - 1] + 1
# else:
# 	LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])