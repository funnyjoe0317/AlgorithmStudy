card, limit = map(int, input().split())
card_num = []
box=[]
compare = []

card_num=list(map(int, input().split()))

# 주어진 것들에서 3개 조합 만들기
def comb(card_num,n):
    result = []
    if n >len(card_num):
        return result
    
    if n == 1:
        for i in card_num:
            result.append([i])
            
    elif n>1:
        for i in range(len(card_num) - n +1):
            for j in comb(card_num[i+1:], n-1):
                result.append([card_num[i]] + j)
                
    return result

box=comb(card_num, 3)

de=[]
ma_x=0
# 3개의 조합 하나로 합쳐서 블랙잭 숫자와 빼서 차이 값이 작은것 min해서 뽑기..?
for i in range(len(box)):
    for j in range(3):
        ma_x += box[i][j]
    if ma_x >limit:
        ma_x = 0
    else:
        de.append(ma_x)
        ma_x=0
            
print(max(de))

