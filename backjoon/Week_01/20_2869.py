
a,b,v=map(int, input().split())
# # 아침에 올라가는 이동량 aM
#  밤에 내려오는 이동량 bM
#  막대기의 높이


c=int(v-a) # 골인지점 전 
d=int(a-b) # 저장되는 개수
count=int(c/d)
mo = int(c%d)

if mo==0:
    print(count+1)
else:
    print(count+2)




# # 순서 아침과 밤의 합 = 1일치 이동량
# # 높이V / 1일치 이동량A-B = 걸린 기간

# day = v/(a-b)
# print(day)
