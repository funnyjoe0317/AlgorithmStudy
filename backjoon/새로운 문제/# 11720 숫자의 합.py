# 11720 숫자의 합
import sys
input= sys.stdin.readline

N = int(input())
sum = 0
num_list = list(map(int, input().rstrip('\n')))

for i in range(len(num_list)):
    sum += num_list[i]

print(sum)
