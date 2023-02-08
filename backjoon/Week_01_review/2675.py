# 2675 문자열 반복
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    R, S = input().split()
    # split()은 문자열을 공백을 기준으로 나누어 리스트로 반환
    R = int(R)
    # 문자열을 정수로 변환
    for j in range(len(S)):
        print(S[j]*R, end='')
        # end=''를 사용하여 줄바꿈을 하지 않음
        # print()는 기본적으로 출력 후 줄바꿈을 수행
    print()

# 0208
