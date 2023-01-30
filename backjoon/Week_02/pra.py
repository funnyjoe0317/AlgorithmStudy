

def matrix_mul(a, b):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for K in range(N):
                result[i][j] += a[i][k] * b[k][j]

    for i in range(N):
        for j in range(N):
            result[i][j] %= 1000

    return result

N,B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
B = bin(B)[2:]

ident_martrix = 