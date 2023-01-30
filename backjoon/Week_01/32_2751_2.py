from collections import deque

n=int(input())
# sorting_list = list(map(int, input().split()))
sorting_list =[]
result=[]


for i in range(n):
    number =int(input())
    sorting_list.append(number)


def radix_sort(nums):
    buckets = [deque() for _ in range(10)]

    max_val = max(nums)
    Q = deque(nums)
    cur_ten = 1

    while max_val >= cur_ten:
        while Q:
            num = Q.popleft()
            buckets[(num // cur_ten) % 10].append(num)

        for bucket in buckets:
            while bucket:
                Q.append(bucket.popleft())

        cur_ten *= 10

    return list(Q)

di=radix_sort(sorting_list)
print(di)
