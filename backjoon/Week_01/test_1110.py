n= str(input())

first_li=[]
new_li=[]
answer=[]
l=[1]
for i in range(len(n)):
    new = int(n[i])
    first_li.append(new)
    new_li=first_li
    for j in range(100):
        if len(new_li)<2:
            new_li.append(0)
            new_li.reverse()
        plus=new_li[0]+new_li[1]
        answer.append(new_li[1])
        answer.append(plus)


# for i in range(100):
#     if len(new_li)<2:
#         new_li.append(0)
#         new_li.reverse()
#     plus=new_li[0]+new_li[1]
#     answer.append(new_li[1])
#     answer.append(plus)
#     if answer==first_li:
#         print[i]
#         break
#     else:
#         pass