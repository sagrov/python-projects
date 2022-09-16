import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-W", type=int)
parser.add_argument("-w", nargs='+', type=int)
parser.add_argument("-n", type=int)
args = parser.parse_args()


def knapsack(W, w, n):
    knapsack_capacity = {}
    for c in range(W+1):
        knapsack_capacity[(0, c)] = 0

    for i in range (1, n+1):
        for c in range(W+1):
            if w[i-1] <= c:
                knapsack_capacity[(i, c)] = max(knapsack_capacity[(i-1, c)], w[i-1] + knapsack_capacity[(i-1, c-w[i-1])])
            else:
                knapsack_capacity[(i, c)] = knapsack_capacity[(i-1, c)]

    print(knapsack_capacity[(n, W)])
    return knapsack_capacity[(n, W)]


knapsack(args.W, args.w, args.n)