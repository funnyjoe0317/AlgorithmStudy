# 카드 놓기 풀이법
# 겹치는 카드도 카운트해서 경우의 수를 구한 후에 중복값을 제거 한다면?

# 재귀함수 순열
card_given = int(input())
card_pick = int(input())
card_number=[]
card_result=[]
number=[]

# 집합 set([]) 중복값 제거 할때 

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


for i in range(card_given):
    number =input()
    card_number.append(number)


card_result=perm(card_number, card_pick)

listd=[]
for i in range(len(card_result)):
    re_card=''.join(card_result[i])
    listd.append(re_card)



final_list=[]
for value in listd:
    if value not in final_list:
        final_list.append(value)

print(len(final_list))

# # 10이상의 카드 뒤집어서 리스트에 넣기
# for i in range(card_given):
    
#     number =int(input())
#     if number >=10:
#         card_number.append(number)
#         # new_card=(number%10)*10+int(number/10)
#         # card_number.append(new_card)
#     else:
#         card_number.append(number)

# print(card_number)

# # 뽑히는 카드 조합짜기
# def comb(arr,n):
#     result = []
#     if n >len(arr):
#         return result
    
#     if n == 1:
#         for i in arr:
#             result.append([i])
            
#     elif n>1:
#         for i in range(len(arr) - n +1):
#             for j in comb(arr[i+1:], n-1):
#                 result.append([arr[i]] + j)
                
#     return result

# card_result=comb(card_number,card_pick)
# card_double = card_result

# # for i in range(len(card_result)):
# #     card_result.reverse()

# # for i in range(len(card_result) // 2):
# #     card_result[i], card_result[-1 - i] = card_result[-1 - i], card_result[i]

# # 내 접근법 데이터가 두개일 경우 앞뒤의 순서를 바꿔서 리스트에 추가하여서 중복값을 제거하면될거라 생각함
# for i in range(len(card_result)):
#     if len(card_result[i][j])==2:
#         for j in range(1):
#             card_result[i][j], card_result[i][j+1] = card_result[i][j+1], card_result[i][j]
#     elif len(card_result[i][j])==3:

# print(card_result)

# finalcard_result=[]
# # 중복값 제거
# # for value in card_result:
# #     if value not in finalcard_result:
# #         finalcard_result.append(value)

# print(len(card_result))
# # print(len(finalcard_result))
