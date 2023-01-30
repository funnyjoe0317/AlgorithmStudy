from array import array


n, m  = map(int, input().split())

array=[]
for i in range(n):
    array.append(int(input()))

# 한번 계산된 결과를 저장하기 위한 dp테이블 초기화
d = [10001] * (m+1)

# 다이나믹 프로그래밍
d[0] = 0
for i in range(n):
    for j in range(array[i],m+1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])