
import sys
input = sys.stdin.readline

new_point=0
N = list(map(int, input().split()))

level_list=[]

for i in range(N[0]):
    level_x = int(input())
    level_list.append(level_x)

point = N[1]

while True:
    if max(level_list)==min(level_list):
        new_point=point//N[0]
        print(min(level_list)+new_point)
        break

    elif point > 1:
        point_give=point//2
        new_level=min(level_list)+point_give
        level_list.append(new_level)
        level_list.remove(min(level_list))
        point=point-point_give

    elif point == 1:
        new_level=min(level_list)+point_give
        level_list.append(new_level)
        level_list.remove(min(level_list))
        point=point-point_give
        
    else:
        print(min(level_list))
        break



