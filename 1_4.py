bars = [30, 20, 10]
vol = 45
len = len(bars)


def knapsack(capacity, weight, n):
    k = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    # Creating a matrix for dp solving.
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                k[i][w] = 0
            # Weight equals to 0.
            elif weight[i-1] <= w:
                k[i][w] = max(weight[i-1] + k[i-1][w-weight[i-1]],  k[i-1][w])
            # Maximum weight in this subset
            else:
                k[i][w] = k[i-1][w]
            # Copy previous value
    return k[n][capacity]


print(knapsack(vol, bars, len))