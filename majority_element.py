# Uses python3
import sys

# sys.stdin = open('input.txt')


def get_majority_element(a, left, right):

    # majority element
    m = None
    count = 0

    for i, x in enumerate(a):
        if i == 0:
            m = x
            count = 1

        else:
            if m == x:
                count += 1

            else:
                if count > 0:
                    count -= 1

                if count == 0:
                    m = x

    count = 0
    for x in a:
        if m == x:
            count += 1

    if count > len(a) // 2:
        return 1

    else:
        return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
