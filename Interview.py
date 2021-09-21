import random


def groupPairs(arr):
    n = len(arr)

    if n == 0:
        return []
    if n == 1:
        return [[arr[0]]]

    res = []

    if n & 1:
        counter = 0
        group = []

        while counter < 3:
            pos = random.randint(0, n-1)
            group.append(arr[pos])

            arr[pos], arr[n-1] = arr[n-1], arr[pos]
            n -= 1

            counter += 1

        res.append(group)

    while n > 0:
        group = []

        pos = random.randint(0, n-1)
        group.append(arr[pos])

        arr[pos], arr[n-1] = arr[n-1], arr[pos]
        n -= 1

        pos = random.randint(0, n-1)
        group.append(arr[pos])

        arr[pos], arr[n-1] = arr[n-1], arr[pos]
        n -= 1

        res.append(group)

    return res


if __name__ == '__main__':
    #groupPairs([1, 2, 3, 4, 5])

    groupPairs([1, 2, 3, 4])
