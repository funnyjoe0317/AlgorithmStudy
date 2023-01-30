def factorial(n:int)->int:
    # -> int 의 이유는?
    if n>0:
        return n*factorial(n-1)
    else:
        return 1
    
n=int(input())
print(factorial(n))