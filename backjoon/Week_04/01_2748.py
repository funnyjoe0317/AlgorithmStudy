# 첫번째 풀이
import collections


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) +fib(n-2)
        # 부루트포스를 이용한 풀이

# 다이나믹 풀이 (메모제이션)
class solution:
    dp = collections.defaultdict(int)

    def fibo(self, n:int)->int:
        if n <= 1:
            return n

        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.fibo(n-1)+self.fibo(n-2)
        return self.dp[n]
        # 부르트포스와 유사하게 재귀로 계산해 나아가지만, 이미 계산한 값은 저장해두었다가 바로 리턴한다.

print(solution(10))

# 타뷸레이션
class solution2:
    dp = collections.defaultdict(int)

    def fibo2(self, n:int)->int:
        self.dp[0] = 0
        self.dp[1] = 1

        for i in range(2, n+1):
            self.dp[i] = self.dp[i-1] +self.dp[i-2]
        return self.dp[n]
        # 재귀를 사용하지 않고 반복으로 풀이하며, 작은 값부터 직접계산하면서
        # 타뷸레이션한다.

# 두 변수만 이용해 공간 절약
def fibo3(self,n):
    x,y = 0,1
    for i in range(0,n):
        x,y = y,x+y
        return x

# 행렬 넘파이를 사용해야 합니다. np = 넘파이
def fibo3(n):
    m = np.martrix([[0,1],[1,1]])
    vec = np.array([[0],[1]])

    return np.matmul(m**n, vec)[0]


