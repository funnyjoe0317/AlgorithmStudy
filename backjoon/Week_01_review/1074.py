# Z 0221
import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

def z_func(N, r, c):
    if N == 0:
        # base case
        return 0
    
    half = 2**(N-1)
    # 1사분면, 2사분면, 3사분면, 4사분면
    if r < half and c < half:
        # 1사분면
        return z_func(N-1, r, c)
    if r < half and c >= half:
        # 2사분면
        return half*half + z_func(N-1, r, c-half)
    if r >= half and c < half:
        # 3사분면
        return 2*half*half + z_func(N-1, r-half, c)
    if r >= half and c >= half:
        # 4사분면
        return 3*half*half + z_func(N-1, r-half, c-half)
    
print(z_func(N, r, c))