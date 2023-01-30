n=int(input())
# sorting_list = list(map(int, input().split()))
sorting_list =[]
result=[]


for i in range(n):
    number =int(input())
    sorting_list.append(number)
    

# 중복값 제거 함수
# for value in sorting_list:
#     if value not in result:
#         result.append(value)

def bubble_sort(a):
    # 버블정렬을 만들어 보자
    n=len(a)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if a[j-1]>a[j]:
                a[j-1],a[j]= a[j], a[j-1]

bubble_sort(sorting_list)

for i in range(len(sorting_list)):
    print(sorting_list[i])

# 50 N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.