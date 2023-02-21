# 전자레인지 0218

import sys
input = sys.stdin.readline

# A = 5분 B = 1분 C = 10초
N = int(input())

Time_list = [300, 60, 10]
cnt_list = [0, 0, 0]


if N%10 != 0:
    print(-1)
else:
    while True:
        if  N // 300 != 0:
            N = N - 300
            cnt_list[0] += 1
        elif N // 60 != 0:
            N = N -60
            cnt_list[1] += 1
        elif N // 10 != 0:
            N = N -10
            cnt_list[2] += 1
        else:
            print(' '.join(map(str, cnt_list)))
            break
