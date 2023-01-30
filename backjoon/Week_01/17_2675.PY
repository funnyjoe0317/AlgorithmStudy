first = int(input())
for i in range(first):
    sec_list=[]
    divide=[]
    sec = input()
    
    sec_list.append(sec)

    divide=sec_list[0].split(" ")
    
    number=divide[0]
    number= int(number)
    text = list(divide[1])
    done_print=[]
    for j in range(len(text)):
        d=number*text[j]
        done_print.append(d)
    str = "".join(done_print)
    print(str)

# 항상 지나가는 i 잘 확인하자