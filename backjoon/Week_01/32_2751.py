
n=int(input())
# sorting_list = list(map(int, input().split()))
sorting_list =[]
result=[]

for i in range(n):
    number =int(input())
    sorting_list.append(number)

def qsort(a,left,right):
    pl = left
    pr = right
    x = a[(left+right) // 2]

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl +=1
            pr-=1
        
    if left < pr:qsort(a, left, pr)
    if pl < right:qsort(a,pl,right)

def quick_sort(a):
    qsort(a,0,len(a)-1)

quick_sort(sorting_list,0,len(sorting_list)-1) 
# 요거 잘써야함

print(sorting_list)


# 다른 퀵정렬
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     lesser_arr, equal_arr, greater_arr = [], [], []
#     for num in arr:
#         if num < pivot:
#             lesser_arr.append(num)
#         elif num > pivot:
#             greater_arr.append(num)
#         else:
#             equal_arr.append(num)
#     return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)
