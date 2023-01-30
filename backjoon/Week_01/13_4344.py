n=int(input())
b=[]
for i in range(n):
    b.append(str(input()))
for i in range(n):
    ans=0
    con = 0
    ans_final=0
    count = b[i].split(' ')
    duple=int(len(count))
    box=[]
    
    
    for j in range(len(count)-1):
        score_sum=int(count[j+1])
        ans=score_sum + ans
        con =con+1
        if con ==len(count)-1:
            ans_final=int(ans/(len(count)-1))
            number_averge=int(ans_final)
            ans=0
            intarr = list(map(int, count))
            for k in range(len(intarr)):
                if intarr[k]>number_averge:
                    box.append(intarr[k])
            len_box = int(len(box))                    
            goal=(len_box/(duple-1))*100
            print("{:.3f}%".format(goal))


# 백준사이트상 틀림/ vscode는 됨
# del 리스트[0] 리스트 0번째 지우기

