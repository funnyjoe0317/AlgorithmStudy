# 11653 소인수 분해
import sys
input= sys.stdin.readline

# n, d =  map(int, input().split())
N = int(input())
#에라토네스의 체를 이용한 풀이는 실패
n=N
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False


k = 0
new = N
if N == 1:
    exit(0)
else:
    while primes[k] <= 997:
        if new == 1:
            break
        elif new % primes[k] == 0:
            new = new / primes[k]
            print(primes[k])
        else:
            k += 1
            if new % primes[k] == 0:
                new = new / primes[k]
                print(primes[k])


# 다른 풀이

N = int(input())

if N == 1:
    print("")

for i in range(2, N+1):
    while N % i ==0:
        print(i)
        N = N / i
        if N == 1:
            break
