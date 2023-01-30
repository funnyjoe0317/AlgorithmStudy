# 아홉 난쟁이 중에 백설공주의 일곱난쟁이를 찾아라
# 조건 일곱난쟁이 키의 합은 100이다.
box = []
arr=[]
print_box=[]
sum_card=0
for i in range(9):
    number =int(input())
    arr.append(number)

# 조합 구현
def comb(arr,n):
    result = []
    if n >len(arr):
        return result
    
    if n == 1:
        for i in arr:
            result.append([i])
            
    elif n>1:
        for i in range(len(arr) - n +1):
            for j in comb(arr[i+1:], n-1):
                result.append([arr[i]] + j)
                
    return result

box=comb(arr,7)

for i in range(len(box)):
    for j in range(7):
        sum_card += box[i][j]
    if sum_card ==100:
        print_box=box[i]
    else:
        sum_card=0


def bubble_sort(a):
    # 버블정렬을 만들어 보자
    n=len(a)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if a[j-1]>a[j]:
                a[j-1],a[j]= a[j], a[j-1]

bubble_sort(print_box)

for i in range(len(print_box)):
    print(print_box[i])