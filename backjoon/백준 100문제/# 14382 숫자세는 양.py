# 숫자세는 양
import sys
input = sys.stdin.readline

N = int(input())

num_dict ={}

num_dict = {key:0 for key in range(0,10)}
# print(num_dict)

for i in range(1,N+1):
    A = int(input())
    num_dict = {key:0 for key in range(0,10)}
    # key, value = num_dict.items()
    if A == 0:
        print(f'Case #{i}: INSOMNIA')
    else:
        T = 1
        for e in str(A):
            num_dict[int(e)] = 1
        while 0 in num_dict.values():
            B=A*T
            for c in str(B):
                num_dict[int(c)] = 1
            T += 1
        print(f'Case #{i}: {B}')
