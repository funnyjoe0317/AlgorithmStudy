# 2908 상수
import sys
input = sys.stdin.readline

a, b = input().split()
a = int(a[::-1])
# 문자열을 뒤집어서 정수로 변환
b = int(b[::-1])

if a > b:
    print(a)
else:
    print(b)
