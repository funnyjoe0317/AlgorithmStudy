import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[float('inf')] * (int((2 * n)** 0.5) + 2) for _ in range(n + 1)]
dp[1][0] = 0
stones = set([int(input()) for _ in range(m)])
print(stones)
for i in range(2, n + 1):
    if i in stones: continue
    for j in range(1, int((2 * i) ** 0.5) + 1):
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1
        print(dp)
answer = min(dp[n])
print(dp)
print(answer if answer != float('inf') else -1)