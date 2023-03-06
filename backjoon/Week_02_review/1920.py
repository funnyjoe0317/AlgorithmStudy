# 1920 0227
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A = sorted(A)

def two_minserch(lst, target):
    left = 0
    right = len(lst)-1

    while left <= right:
        mid =(left+right)//2
        if lst[mid] == target:
            return 1
        else:
            if target < lst[mid]:
                right = mid-1
            else:
                left = mid+1
    return 0

K = int(input())
B = list(map(int, input().split()))

for i in range(K):
    print(two_minserch(A, B[i]))
