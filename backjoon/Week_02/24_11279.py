import sys
import heapq

numbers = int(input())
heap = []

#Max Heap
for _ in range(numbers):
    num = int(sys.stdin.readline())

    if num != 0:
        heapq.heappush(heap, (-num))
        # 왜 -num 값을 받는거지?
    else:
        try:
            print(-1 * heapq.heappop(heap))
            # 다시 -1 해줘서 받넹

        except:
            # 입력값이 0 일경우에 위에 try 가 작동되지 않아서
            # 예외로 프린트0을 해주는 거다
            print(0)