
import heapq

N = int(input())

card = []
plus_heap =0
for i in range(N):
    heapq.heappush(card, int(input()))

for i in range(N-1):
    plus=heapq.heappop(card) +heapq.heappop(card)
    heapq.heappush(card, plus)
    plus_heap += plus

print(plus_heap)
