# 몇개의 정수를 받을건지
number=int(input())

# 
n=1000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

# 정수 입력 int로 받아서 알아서 리스트 생긴다
h_list = list(map(int, input().split()))

answer=0

for i in range(len(h_list)):
    if h_list[i] in primes:
        
        answer = 1+answer
        

print(answer)
