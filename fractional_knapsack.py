# Uses python3
import sys

#sys.stdin = open('input.txt')


def get_optimal_value(capacity, weights, values):
    res = 0.
    # write your code here

    items = [(value, weight) for value, weight in zip(values, weights)]

    items.sort(key=lambda x: x[0]/x[1], reverse=True)

    for value, weight in items:

        if capacity > weight:
            res += value
            capacity -= weight

        else:
            res += capacity * value / weight
            break

    return res


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
