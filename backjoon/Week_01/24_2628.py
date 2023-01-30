
x,y=map(int, input().split())
divide= int(input())
width_x_list=[]
width_y_list=[]
divide_list_y=[0,y]
divide_list_x=[0,x]
cut_point=[]

for i in range(divide):
    point=list(map(int, input().split()))
    cut_point.append(point)
    

for j in range(divide):
    # 가로세로 판별
    if cut_point[j][0]==0:
        divide_list_y.append(cut_point[j][1])
        divide_list_y.sort()

    else:
        divide_list_x.append(cut_point[j][1])
        divide_list_x.sort()


    # 가로세로 판별


for i in range(len(divide_list_y)-1):
    width_y_list.append(divide_list_y[i+1]-divide_list_y[i])

for i in range(len(divide_list_x)-1):
    width_x_list.append(divide_list_x[i+1]-divide_list_x[i])

print(width_x_list)
print(width_y_list)

print(max(width_x_list)*max(width_y_list))
