import argparse
import time

# importing arguments
parser = argparse.ArgumentParser()
parser.add_argument("-W", type=int)
parser.add_argument("-w", nargs='+', type=int)
parser.add_argument("-n", type=int)
args = parser.parse_args()


def knapsack(W, w, n):
    print(time.perf_counter())
    knapsack_capacity = {}      # dictionary to store weight values
    for c in range(W+1):
        knapsack_capacity[(0, c)] = 0       # filling the first row with zeroes
    for i in range(1, n+1):
        for c in range(W+1):
            if w[i-1] <= c:
                # fills with max value between element from the same column but 1 row above
                # and weight + value from one row above and c-w elements to the left
                knapsack_capacity[(i, c)] = max(knapsack_capacity[(i-1, c)], w[i-1] + knapsack_capacity[(i-1, c-w[i-1])])
            else:
                # fills with values for the same column and row above
                knapsack_capacity[(i, c)] = knapsack_capacity[(i-1, c)]
    print (time.perf_counter())
    return knapsack_capacity[(n, W)]


print(knapsack(args.W, args.w, args.n))