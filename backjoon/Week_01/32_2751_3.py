def sort3(a, idx1:int, idx2:int, idx3:int):
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    if a[idx3] < a[idx2]: a[idx3], a[idx2] = a[idx2], a[idx3]
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    return idx2

def insertion_sort(a, left:int, right:int):
    # 9개 이하일 때 단순 삽입정렬로 진행
    for i in range(left+1, right+1):
        j=i
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -=1
        a[j]=tmp

def qsort(a, left:int, right:int):
    if right - left <9:
        insertion_sort(a, left, right)
    else:
        pl = left
        pr = right
        m= sort3(a, pl, (pl+pr)//2,pr)
        x = a[m]

        a[m], a[pr-1]=a[pr -1], a[m]
        pl += 1
        pr -= 2
        while pl <= pr:
            while a[pl] < x: pl +=1
            while a[pr] > x: pr -=1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl+=1
                pr-=1

            if left < pr:qsort(a, left, pr)
            if pl<right:qsort(a, pl,right)

n=int(input())
# sorting_list = list(map(int, input().split()))
sorting_list =[]
result=[]

for i in range(n):
    number =int(input())
    sorting_list.append(number)

def quick_sort(a):
    qsort(a,0,len(a)-1)

print(sorting_list)
quick_sort(sorting_list)

print(sorting_list)

