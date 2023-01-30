cargo = [
    (4,12),
    (2,1),
    (10,4),
    (1,1),
    (2,2)
]

def zero_one_(cargo):
    capacity = 15
    pack = []

    for i in range(len(cargo)+1):
        pack.append([])
        for j in range(capacity +1):
            if i ==0 or j == 0:
                pack[i].append(0)
            elif cargo[i-1][1]<= j:
                pack[i].append(
                    max(
                        cargo[i-1][0] + pack[i-1][j-cargo[i-1][1]],
                        pack[i-1][j]
                    )
                )
            else:
                pack[i].append(pack[i-1][j])

    return pack[-1][-1]

print(zero_one_(cargo))

# 그리디 알고리즘 (분할정복 풀이)
def knapsack2(W, w, p):
    n = len(w) -1
    k = [0] * [n+1]
    weight = 0
    for i in range(1, n+1):
        weight += w[i]
        k[i] = w[i]
        if(weight > W):
            k[i] = w[i]
            break
    return k



# 동적 계획법
def knapsack2(i, W, w, p):
    if (i <= 0 or W <= 0):
        return 0
    if (w[i] > W):
        value = knapsack2(i - 1, W, w, p)
        print(i - 1, W, value)
        return value
    else: # w[i] <= W
        left = knapsack2(i - 1, W, w, p)
        print(i - 1, W, left)
        right = knapsack2(i - 1, W - w[i], w, p)
        print(i - 1, W - w[i], right)
        return max(left, p[i] + right)

# 백트래킹 풀이
def knapsack3 (i, profit, weight):
    global maxprofit, numbest, bestset
    if (weight <= W and profit > maxprofit):
        maxprofit = profit
        numbest = i
        bestset = include[:]
    if (promising(i, profit, weight)):
        include[i + 1] = True
        knapsack3(i + 1, profit + p[i+1], weight + w[i+1])
        include[i + 1] = False
        knapsack3(i + 1, profit, weight)

def promising (i, profit, weight):
    if (weight > W):
        return False
    else:
        j = i + 1
        bound = profit
        totweight = weight
        while (j <= n and totweight + w[j] <= W):
            totweight += w[j]
            bound += p[j]
            j += 1
        k = j
        if (k <= n):
            bound += (W - totweight) * p[k] / w[k]
        return bound > maxprofit