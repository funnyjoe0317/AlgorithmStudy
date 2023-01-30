# 알아서 공백을 분리하여 리스트에 넣는다
w,d =input().split()

# 문자열을 하나하나 리스트화 ['3','8',''9~~]
re_w = list(w)
re_d = list(d)
# 하나하나의 리스트를 반대 순서로 변환 ex)389->983
re_w.reverse()
re_d.reverse()
# "9","8","3"의 리스트를 -> "983"으로 변환
re_w2=''.join(re_w)
re_d2=''.join(re_d)
# '983'의 문자열을 정수화 983으로
re_w2 = int(re_w2)
re_d2= int(re_d2)
# if문을 이용하여 대소 판별 후 출력
if re_w2>re_d2:
    print(re_w2)
else:
    print(re_d2)
    
# [::-1] 문자열 