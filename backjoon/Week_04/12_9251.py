# 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열중
# 모두의 부분 수열이 되는 수열중 가장 긴것을 찾는 문제이다.



if i == 0 or j == 0:  # 마진 설정
	LCS[i][j] = 0
elif string_A[i] == string_B[j]:
	LCS[i][j] = LCS[i - 1][j - 1] + 1
else:
	LCS[i][j] = 0