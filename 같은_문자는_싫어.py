# 내 풀이 
def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    compare = arr[0]
    answer.append(compare)
    for i in range(len(arr)):
        # len(arr) must be down?
        # save the value and compare
        if compare != arr[i]:
            # here the problem why?
            compare = arr[i]
            answer.append(compare)
        else:
            continue
    return answer

# 다른 사람 풀이
def no_continuous(s):
    # 함수를 완성하세요
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a