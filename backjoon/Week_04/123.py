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