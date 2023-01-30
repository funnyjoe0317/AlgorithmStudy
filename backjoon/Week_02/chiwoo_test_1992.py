import sys
input= sys.stdin.readline

N=int(input())

A=[]
for i in range(N):
    A.append(list(map(int,input().strip())))

def check_(a,b,W):    
    std=A[a][b]
    for i in range(a,a+W):
        for j in range(b,b+W):
            if std !=A[i][j]:
                print("(",end="")
                check_(a,b,W//2) #1사분면
                check_(a,b+W//2,W//2) #2사분면
                check_(a+W//2,b,W//2) # 3사분면
                check_(a+W//2,b+W//2,W//2) # 4사분면
                print(")",end="")
                return 

    print(std,end="")



check_(0,0,N)