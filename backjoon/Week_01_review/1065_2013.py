# 1065 한수

def is_hansu(n):
    # n이 한수인지 판별하는 함수
    # 한수이면 True, 아니면 False를 반환한다.
    # n은 1 이상 1000 이하의 자연수이다.
    # 한수는 각 자리수가 등차수열을 이루는 수이다.
    # 예를 들어, 123, 456, 789는 한수이다.
    if n < 100:
        return True
    else:
        nums = list(map(int, str(n)))
        # nums를 문자열로 바꾸고, 각 자리수를 int로 바꾼다.
        if nums[0] - nums[1] == nums[1] - nums[2]:
            # 각 자리수의 차이가 같으면 한수이다.
            return True
        else:
            return False

N = int(input())
answer = 0
for i in range(1, N+1):
    if is_hansu(i):
        answer += 1

print(answer)