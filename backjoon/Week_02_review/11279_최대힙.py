# 최대 힙

import sys
input = sys.stdin.readline

N = int(input())
heap = []

def heapify(heap):
    for i in range(len(heap)-1, 0, -1):
        if heap[i] > heap[(i-1)//2]:
            heap[i], heap[(i-1)//2] = heap[(i-1)//2], heap[i]
        else:
            break
