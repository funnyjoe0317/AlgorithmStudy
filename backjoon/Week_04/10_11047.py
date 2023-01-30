# N종류의 동전을 가지고있고, 그 동전들을 합해서 K원을 만들려 한다
# 이때 필요한 동전의 개수의 최솟값 구하기
# 첫째줄에 N과 K가 주어진다.

# N개의 줄에 동전의 가치 A가 오름차순으로 주어짐

import sys

input = sys.stdin.readline
n, coin_target = map(int, input().split())
cnt=0
coin_li =[]

for i in range(n):
    how_much = int(input())
    coin_li.append(how_much)

# print(coin_li)
coin_li.sort(reverse=True)
# print(coin_li)

for coin in coin_li:
    cnt += coin_target // coin
    coin_target %= coin 

print(cnt)


coin_number,won = map(int,input().split())
coin = [int(input()) for _ in range(coin_number)]
coin.sort(reverse=True)
count = 0
for i in range(coin_number):
    if won == 0:
        break
    elif coin[i] <= won:
        count += won // coin[i]
        won = won % coin[i]
    else:
        continue
# print(coin)
print(count)