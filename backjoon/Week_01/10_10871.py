
x = input()
y = input()
x=int(x)
y=int(y)
num = list(map(int, input().split()))

for i in range(x):
    if num[i] <y:
        print(num[i], end=" ")



# a[0:2]