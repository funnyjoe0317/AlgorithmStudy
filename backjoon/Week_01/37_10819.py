
n = int(input())
li = []

li = list(map(int, input().split()))

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

di=perm(li,n)
answer=0
final_answer =0
final_list=[]

for i in range(len(di)):
    for j in range(len(di[i])-1):
        answer=di[i][j] - di[i][j+1]
        final_answer += abs(answer)
        answer=0
    final_list.append(final_answer)
    final_answer=0

print(max(final_list))

        


# 실패
# n = int(input())
# li = []

# li = list(map(int, input().split()))

# bi=[]
# bi=sorted(li)

# answer=0
# answer_final=0

# for i in range(len(bi)//2):
#     answer=bi[i]-bi[len(bi)-(i+1)]
#     answer_final+=abs(answer)
#     if i<len(bi)//2:
#         answer= bi[len(bi)-(i+1)] -bi[i+1]
#         answer_final+=abs(answer)
 
#     answer=0

# print(answer_final)