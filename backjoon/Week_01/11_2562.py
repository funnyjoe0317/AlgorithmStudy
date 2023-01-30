a=[]
for i in range(1,10):
    num = int(input())
    a.append(num)

print(max(a))
indexx=a.index(max(a))
indexx = int(indexx)
print(indexx+1)

