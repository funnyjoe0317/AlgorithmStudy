import collections
import sys

dp = collections.defaultdict(int)

input = sys.stdin.readline
n = int(input())

# def fibo(n):
#     if n <=1:
#         return n

#     if dp[n]:
#         return dp[n]
#     dp[n] = fibo(n-1)+fibo(n-2)
#     return dp[n]

# print(fibo(n))

# if dp[n]은 딕셔너리 내부에 원래 계산된것이 있다면 넘어가게 하여서 시간을 절약하는 것이다.
# fibo(n-1)이랑 fibo(n-2)랑 같이 호출되면 두개가 호출되는 건가?


dp = collections.defaultdict(int)

def fibo2( n:int)->int:
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

print(fibo2(n))


def fibo3(n):
    x,y = 0,1
    for i in range(0,n):
        x,y = y,x+y
        return x

print(fibo3(n))