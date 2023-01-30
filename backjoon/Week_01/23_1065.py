num = int(input())

answer = 0

if num <100:
    print(num)
elif num<1000:
    ten = (num//10)//10
    one = num%10
    for i in range(1,9):
        if ten == i:
            answer = ((num//100)-1)*5
            for j in range(1,9):
                if one == j:
                    
                    answer += 1

    answer= answer+num

print(answer)

# 나중에 다른사람 풀이 확인하기

# 지수형 풀이 부르트 포스로 접근
N = int(input())
cnt = 0
for i in range(1,N+1):
    if len(str(i)) == 1 or len(str(i)) == 2:
        cnt += 1
    elif len(str(i)) == 3:
        A = list(str(i))
        A = [int(i) for i in A]
        if A[0]-A[1] == (A[1]-A[2]):
            cnt += 1
    else:
        B = list(str(i))
        B = [int(i) for i in B]
        if B[0]-B[1] == B[1]-B[2] == B[2]-B[3]:
            cnt += 1
print(cnt)