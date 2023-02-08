# 11816 8진수, 10진수, 16진수
import sys
input= sys.stdin.readline

num_list = list(map(str, input().rstrip('\n')))

if num_list[0] == "0":
    if num_list[1] == "x":
        num_list = ''.join(num_list)
        num_list = int(num_list, 16)
        print(num_list)
    else:
        num_list = ''.join(num_list)
        num_list = int(num_list, 8)
        print(num_list)
else:
    num_list = ''.join(num_list)
    print(num_list)  
