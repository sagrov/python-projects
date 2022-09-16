import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-W", type=int)
parser.add_argument("-w", nargs='+', type=int)
parser.add_argument("-n", type=int)
args = parser.parse_args()


def knapsack(W, w, n):
    N = len(w)
    m = {}
    for c in range(W+1):
        m[(0, c)] = 0

    for i in range (1, n+1):
        for c in range(W+1):
            if w[i-1] <= c:
                m[(i, c)] = max(m[(i-1, c)], w[i-1] + m[(i-1, c-w[i-1])])
            else:
                m[(i, c)] = m[(i-1, c)]

    print(m[(N, W)])
    return m[(N, W)]


knapsack(args.W, args.w, args.n)