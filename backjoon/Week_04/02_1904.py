import sys

input = sys.stdin.readline
n = int(input())

dp = [0] * 1000001

def fibo2( n:int)->int:
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = (dp[i-1] +dp[i-2])%15746
        return dp[n]

print(fibo2(n))

# 두 변수만 이용해 공간 절약
# def fibo3(n):
#     x,y = 0,1
#     for i in range(0,n+1):
#         x,y = y,x+y
#     return x

# print(fibo3(n))