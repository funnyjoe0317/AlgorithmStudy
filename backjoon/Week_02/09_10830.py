
import sys
input = sys.stdin.readline
N,K = map(int,input().split())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def divide_num(matrix,K):
    if K == 1:
        return matrix
    else:
        matrix_mul = divide_num(matrix, K-1)
        if K == 
        productmatrix(matrix_mul,matrix_mul)
        
    # for i in range(len(matrix)-1):
    #     for j in range(len(matrix)-1):



def productmatrix(A,B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
        

print(matrix)