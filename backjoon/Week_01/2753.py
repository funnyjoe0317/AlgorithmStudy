a= input()
a = int(a)

b=a%400
c=a%100
d=a%4

if d ==0:
    if b==0:
        if c ==0:
            print("1")
    elif c==0:
        print("0")
    else:
        print("1")
else:
    print("0")

    # 윤년문제