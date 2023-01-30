# N개의 물건이 있는데 무게는 W 이고, value is V
# 물건 가치가 최대가 되는 K를 구하여라
# 짐을 쪼갤수 있는 경우 분할가능 배낭 문제, 짐을 쪼갤수 없는 경우 0-1 배낭문제

# 점화식 DP[i][j] = max(DP[i -1][j], DP[i-1][j-W[i]]+V[i] )

n, k = map(int, input().split())

thing = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    thing.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = thing[i][0]
        v = thing[i][1]

        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][k])
