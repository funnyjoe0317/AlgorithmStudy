# 공유기를 양끝에 설치하고 남은 공유기를 가운데에 설치 후 이분탐색으로
# 왼쪽가운데 오른쪽 가운데 설치하면 되냐?
import sys
input = sys.stdin.readline
# 집의 개수와 공유기 설치 대수
N = list(map(int, input().split()))
home_list=[]

result = 0
#  집의 x좌표의 위치 인풋
for i in range(N[0]):
    home_x = int(input())
    home_list.append(home_x)
home_list.sort()
# 리스트에 넣고 순서에 맞게

# 이분탐색 시작과 끝
# [1,2,4,8,9,10]
wifi_list =[home_list[0],max(home_list)]
# 공유기 설치는 처음과 마지막에 무조건 설치되야 함으로 미리 설정
if N[1] == 2:
    print(home_list[N[0]-1] - home_list[0])

else:
    while(len(wifi_list) < N[1]):
        
        if len(home_list)%2 ==0:
            wifi_point=home_list[(len(home_list)//2)-1]
            wifi_list.append(wifi_point)
            wifi_list.sort()
        else:
            wifi_point=home_list[len(home_list)//2]
            wifi_list.append(wifi_point)
            wifi_list.sort()
        

        if max(wifi_list)-wifi_point > wifi_point-min(wifi_list):
                home_list[len(home_list)//2:]
                # 확인완료
        else:
            if len(home_list)%2 ==0:
                home_list[:(len(home_list)//2)]
                print(home_list)
            else:
                home_list[:len(home_list)//2+1]
                print(home_list)

        # mid = (start + end) // 2
        # 공유기를 설치한다 가정하자

print(wifi_list[1]-wifi_list[0])

