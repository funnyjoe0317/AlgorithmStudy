import sys
# sys.stdin = open('BOJ/input.txt', 'r')
input = sys.stdin.readline

N = str(int(input()))

count = 0
if len(N) < 2:
    N = N + '0'

def do_cycle(number):
    global N
    global count

    str_digits =[]
    for idx in range(len(number)):
        str_digits.append(number[idx])
    int_digits = list(map(int, str_digits))
    new_number = str_digits[1]+str(sum(int_digits))[-1]
    count += 1
    if new_number == N:
        return 
    do_cycle(new_number)

do_cycle(N)
print(count)