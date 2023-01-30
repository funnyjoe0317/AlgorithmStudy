from collections import deque
import sys
input = sys.stdin.readline
N=int(input())

Q=deque([])

for i in range(N):
    command = input().split()
    if command[0] == 'push':
        Q.append(command[1])
    elif command[0] == 'front':
        if len(Q) == 0:
            print('-1')
        else:
            print(Q[0])
    elif command[0] == 'back':
        if len(Q) == 0:
            print('-1')
        else:
            print(Q[len(Q)-1])
    elif command[0] == 'size':
        print(len(Q))
    elif command[0] == 'empty':
        if len(Q) == 0:
            print('1')
        else:
            print('0')
    elif command[0] == 'pop':
        if not Q:
            print(-1)
        else:
            print(Q.popleft())
        
