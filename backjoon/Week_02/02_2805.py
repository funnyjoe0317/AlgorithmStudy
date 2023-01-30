
# 시간초과 샤발

import sys
input = sys.stdin.readline

def bin_search(a,key):
    global N
    global tree_taken
    pl = 0
    pr = max(li)

    while True:
        pc = (pl +pr) // 2
        for i in range(len(li)):
            if li[i]>height_li[pc-1]:
                tree_taken +=li[i]-(height_li[pc]-1)

        if tree_taken == key:
            return print(height_li[pc]-1)
        elif key <tree_taken:
            pl = pc
            tree_taken=0
        else:
            pr = pc
            tree_taken=0
        if pl > pr:
            break

N = list(map(int, input().split()))
tree_taken=0
tree_get = N[1]
height_li = []

li= list(map(int, input().split()))

for i in range(1,max(li)+1):
    height_li.append(int(i))

li.sort()

bin_search(height_li, tree_get)
