# 2447 별 찍기 - 10
# 문제
# 크기가 N×N인 패턴은 가로, 세로 길이가 N인 정사각형으로 이루어져 있다. 크기가 3×3인 패턴은 가로, 세로 길이가 3인 정사각형 9개로 이루어져 있고, 크기가 9×9인 패턴은 가로, 세로 길이가 9인 정사각형으로 이루어져 있다.

# ***************************
# * ** ** ** ** ** ** ** ** *
# ***************************
# ***   ******   ******   ***
# * *   * ** *   * ** *   * *
# ***   ******   ******   ***
# ***************************
# * ** ** ** ** ** ** ** ** *
# ***************************
# *********         *********
# * ** ** *         * ** ** *
# *********         *********
# ***   ***         ***   ***
# * *   * *         * *   * *
# ***   ***         ***   ***
# *********         *********
# * ** ** *         * ** ** *
# *********         *********
# ***************************
# * ** ** ** ** ** ** ** ** *
# ***************************
# ***   ******   ******   ***
# * *   * ** *   * ** *   * *
# ***   ******   ******   ***
# ***************************
# * ** ** ** ** ** ** ** ** *
# ***************************

# 패턴을 보면 상하좌우 대칭 3으로 나누었을때 이런식 만들어보라 
# 분할정복과 재귀 개념 다시 공부

# 분할정복
# 분할정복은 문제를 나눌 수 없을 때까지 나누어서 각각을 풀면서 다시 합병하여 문제의 답을 얻는 알고리즘 설계 기법이다. 분할정복은 다음과 같은 순서로 이루어진다.

# divide and conquer
# 1. Divide: 주어진 문제를 같은 크기의 부분 문제로 나눈다.
# 2. Conquer: 나눠진 부분 문제를 재귀를 이용하여 푼다.
# 3. Combine: 푼 부분 문제를 합쳐(Combine) 원래 문제에 대한 답을 얻는다.

# 재귀

# 재귀란 자기 자신을 호출하는 함수를 의미한다. 재귀 함수는 자기 자신을 호출하고, 이 때 전달되는 인자의 값이 조건에 따라 달라지도록 작성되어야 한다. 재귀 함수는 종료 조건이 반드시 필요하다. 종료 조건이 없다면 함수는 무한히 호출되어 스택 오버플로우가 발생할 수 있다.

import sys
input= sys.stdin.readline

# N = int(input())
# star = [[' ' for _ in range(N)] for _ in range(N)]

# print(star)

# def star10(x,y,N):
#     if N == 1:
#         star[x][y] = '*'
#         return
#     div = N//3
#     for i in range(3):
#         for j in range(3):
#             if i == 1 and j == 1:
#                 continue
#             star10(x+div*i, y+div*j, div)

# print(star10(0,0,N))
n = int(input())

def star(l):
    if l == 3:
        return ['***','* *','***']

    arr = star(l//3)
    stars = []

    for i in arr:
        stars.append(i*3)

    for i in arr:
        stars.append(i+' '*(l//3)+i)

    for i in arr:
        stars.append(i*3)

    return stars

print('\n'.join(star(n)))
