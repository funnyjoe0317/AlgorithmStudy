

def bin_search(a,key):
    # 서치를 할 리스트 a 와 찾고자 하는  값 key를 매개변수로 받는다.
    global N
    # N은 문제에서 N개의 정수를 받아야하기에 함수에서 전역변수로 설정
    global tree_taken
    # 트리는
    pl = 0
    pr = max(li)

    while True:
        pc = (pl +pr) // 2
        for i in range(len(li)):
            if li[i]>height_li[pc]:
                tree_taken +=li[i]-height_li[pc]

        if tree_taken == key:
            return print(height_li[pc])
        elif a[pc] <tree_taken:
            pl = pc+1
            tree_taken=0
        else:
            pr = pc -1
            tree_taken=0
        if pl > pr:
            break


N = list(map(int, input().split()))
tree_get=N[1]
li= list(map(int, input().split()))
height_li = []
for i in range(1,max(li)):
    height_li.append(int(i))

li.sort()

bin_search(height_li, tree_get)


