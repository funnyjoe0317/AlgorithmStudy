a = list('OOXXOOXOXO')

score = 0
yeonsok = 0

for i in range(len(a)):
    if a[i] == 'O':
        yeonsok = yeonsok + 1
        score = score + yeonsok
    else:
        yeonsok = 0

print(score)