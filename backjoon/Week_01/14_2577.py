A=input()
B=input()
C=input()
A = int(A)
B = int(B)
C = int(C)

ABC = A*B*C
ABC = str(ABC)
CBA = list(ABC)

for i in range (10):
    H = str(i)
    print(CBA.count(H))



# clear!