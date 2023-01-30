#Merge Sort 병합 정렬을 이용한 풀이
def merge(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = merge(array[:mid])
    right = merge(array[mid:])
    
    return merge_func(left, right)

def merge_func(left, right):
    merge_list = []
    left_id, right_id = 0, 0
    
    #case1 left, right
    while len(left) > left_id and len(right) > right_id:
        if left[left_id] > right[right_id]:
            merge_list.append(right[right_id])
            right_id += 1
        else:
            merge_list.append(left[left_id])
            left_id += 1
    
    #case2 letf
    while len(left) > left_id and len(right) <= right_id:
        merge_list.append(left[left_id])
        left_id += 1
    
    #case3 right
    while len(right) > right_id and len(left) <= left_id:
        merge_list.append(right[right_id])
        right_id += 1
    
    return merge_list

import sys
n = int(input())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))

li = merge(li)

for i in li:
    print(i)