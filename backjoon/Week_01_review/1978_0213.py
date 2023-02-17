# 소수 찾기
# 소수를 찾는 방법은 여러가지가 있다.
# 1. 에라토스테네스의 체
# 2. 소수의 배수를 제거하는 방법

# 1. 에라토스테네스의 체

# 1. 2부터 N까지의 모든 자연수를 나열한다.
# 2. 남은 수 중 아직 처리하지 않은 가장 작은 수 i를 찾는다.
# 3. 남은 수 중 i의 배수를 모두 제거한다. (i는 제거하지 않는다.)
# 4. 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복한다.

import math
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

nums = sorted(nums)

def eratos(n):
    sieve = [True] * n

    m = int(n**0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

eratos_list = eratos(1000000)
answer = 0
for i in range(N):
    if nums[i] in eratos_list:
        answer += 1 

print(answer)