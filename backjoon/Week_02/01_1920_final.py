
import sys

N = int(sys.stdin.readline().rstrip())
# sys로 받을 때 뒤에 값 줄넘김 없애는  방법 rstrip()
number_li =list(map(int, sys.stdin.readline().rstrip().split()))
# 숫자 값을 한번에 받을 때 사용하는 법
number_li.sort()
K = int(sys.stdin.readline().rstrip())
search_li = list(map(int, sys.stdin.readline().rstrip().split()))

# def bin_search(a, key):
#     global N
#     start = 0
#     end = len(number_li) - 1

#     while start >=end: 
#         mid  = (start+ end) //2
#         if mid == key:
#             return mid
#         elif mid > key:
#             start = mid -1
#         else:
#             end = mid +1
# 기본형식의 이진탐색
 
for i in range(len(search_li)):


    start = 0
    end = len(number_li) - 1

    while True:
        mid= (start + end) //2
        if number_li[mid] == search_li[i]:
            print(1)
            break
        elif number_li[mid] > search_li[i]:
            end = mid-1
        else:
            start = mid+1
        if start>end:
            print(0)
            break








