# import sys
# input = sys.stdin.readline
# N = list(map(int,input().split()))

# # number = N[0]
# # blackpink_jisu = N[1]
# # divide = N[2]

# def jisu(N):
#     if N[0]<N[2]:
#         if N[0]**N[1]>N[2]:
#             print((N[0]**2) % N[2])
#         else:
#             print(N[0])
#     elif N[0]>N[2]:
#         print(N[0]-N[2])
#     else:
#         print(0)
#     # print((N[0]**(N[1]))%N[2])


# jisu(N)



# a,b,c=map(int,input().split())

# def divide_num(a,b):
#     if b == 1:
#         return a%c
#     else:
#         given_num = divide_num(a,b//2)
#         if b%2 ==0:
#             return(given_num*given_num)%c
#         else:
#             return(given_num*given_num*a)%c

# print(divide_num(a,b))

a,b,c=map(int,input().split())

def divide_num(a,b):
    if b == 1:
        return a%c
    else:
        given_num = divide_num(a,b//2)
        if b%2 ==0:
            return(given_num*given_num)%c
        else:
            return(given_num*given_num*a)%c

print(divide_num(a,b))