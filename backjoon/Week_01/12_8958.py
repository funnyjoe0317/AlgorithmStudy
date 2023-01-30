a= int(input())
b=[]
dic=[]
for i in range(a):
    
    b.append(str(input()))

last=0

for i in range(len(b)):
    a = 0
    dic=b[i].split('X')
    for j in range(len(dic)):
        summ=len(dic[j])
        summ=int(summ)
        last = (summ+1)*summ/2 + last
        a = a+1
        if a == len(dic):
            print(last)
            last = 0

# 소수점 때문이다