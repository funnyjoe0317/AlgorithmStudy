
# 조합
def comb(arr,n):
    result = []
    if n >len(arr):
        return result
    
    if n == 1:
        for i in arr:
            result.append([i])
            
    elif n>1:
        for i in range(len(arr) - n +1):
            for j in comb(arr[i+1:], n-1):
                result.append([arr[i]] + j)
                
    return result

# 순열
def perm(arr, n):
    result =[]
    if n > len(arr):
        return result
    
    if n==1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for p in perm(ans, n-1):
                result.append([arr[i]]+p)

    return result

rotto_list=[]
de=[]

for i in range(49):
    li = list(map(int, input().split()))
    de.append(li)
    if len(li)==1:
        break

for i in range(len(de)):
    del de[i][0]

for i in range(len(de)-1):
    rotto_list=comb(de[i],6)

for i in range(len(rotto_list)):
    print(rotto_list[i])



# for i in range(1,49):
#     rotto_list.append(i)



