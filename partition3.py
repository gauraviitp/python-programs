# Uses python3
import sys

#sys.stdin = open('input.txt')


def partition3(A):

    s = sum(A)
    bitset = 1

    for a in A:

        bitset = bitset << a | bitset

    return 1 if s % 3 == 0 and bitset >> (s // 3) & 1 == 1 and bitset >> (2 * s // 3) & 1 == 1 else 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))
