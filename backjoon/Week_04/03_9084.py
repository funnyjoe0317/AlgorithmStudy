# 1,5,10,50,100,500원이 있는데 이 동전들로는 정수의 금액 만들기 가능
# 입력 첫줄에는 테스트케이스 T,


# 3 얘가 T 테스트 케이스 3번 한다 이런의미
# 2 동전의 가지수
# 1 2 동전의 종류
# 1000 원하는 금액
# 3 동전의 가지수
# 1 5 10 동전의 종류
# 100  금액
# 2 같음
# 5 7
# 22

# 출력은 N가지 동전으로 금액 M을 만드는 모든 방법의 수를 한줄에 하나씩 출력

# import sys

# input = sys.stdin.readline
# N = int(input())

# def count(coin_li):


# for i in range(N):
#     coin_num = int(input())
#     coin_li = list(map(int, input().rstrip().split()))
#     coin = int(input())

#     print(count(coin_li))


def test():
    test_case = int(input())
    for i in range(test_case):
        coin_number = int(input())
        coin = list(map(int, input().split()))
        total = int(input())
        dp = [0 for i in range(total + 1)]
        dp[0] = 1
        for k in coin:
            for j in range(1, total + 1):
                if j - k >= 0:
                    dp[j] += dp[j - k]
        print(dp[total])
test()
