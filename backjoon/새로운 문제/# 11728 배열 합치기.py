# 11728 배열 합치기
import sys
input= sys.stdin.readline

# 첫째 줄에 배열 A의 크기 N, 배열 B의 크기 M이 주어진다. 
N = list(map(int, input().split()))

# 리스트 생성 생성하면서 input받기
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

# 리스트 합치기
sum_list = A_list + B_list
sum_list = sorted(sum_list)

#프린트할 때 *랑 같이 프린트하면 ["abc"] -> abc 로 출력된다.
print(*sum_list)
