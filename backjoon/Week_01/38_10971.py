n = int(input())
some=[]
some_cost =[]
use=[]

for i in range(n-1):
    some.append(i)


for i in range(n):
    li = list(map(int, input().split()))
    some_cost.append(li)

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

use=perm(some, len(some))
cost_total=0
cost=[]

for i in range(len(use)):
    for j in range(n):
        if j == n-1:
            cost_total+=some_cost[use[i][j]][use[i][0]]
            cost.append(cost_total)
            cost_total=0
        else:
            cost_total+=some_cost[use[i][j]][use[i][j+1]]
            pass

print(min(cost))
