import functools
from enum import Enum


def binary_search(nums, target):
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            hi = mid-1
        elif target > nums[mid]:
            lo = mid+1
    return lo


class State(Enum):
    S = 0
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8
    I = 9


def transition(state, c):
    next = state
    if state == State.S:
        if c.isdigit():
            next = State.A
        elif c == '+' or c == '-':
            next = State.I
        elif c == '.':
            next = State.B
        else:
            next = State.C
    elif state == State.A:
        if c.isdigit():
            next = State.A
        elif c == '.':
            next = State.G
        elif c == 'e':
            next = State.D
        else:
            next = State.C
    elif state == State.B:
        if c.isdigit():
            next = State.H
        else:
            next = State.C
    elif state == State.C:
        next = State.C
    elif state == State.D:
        if c.isdigit():
            next = State.F
        elif c == '+' or c == '-':
            next = State.E
        else:
            next = State.C
    elif state == State.E:
        if c.isdigit():
            next = State.F
        else:
            next = State.C
    elif state == State.F:
        if c.isdigit():
            next = State.F
        else:
            next = State.C
    elif state == State.G:
        if c.isdigit():
            next = State.H
        elif c == 'e':
            next = State.D
        else:
            next = State.C
    elif state == State.H:
        if c.isdigit():
            next = State.H
        elif c == 'e':
            next = State.D
        else:
            next = State.C
    elif state == State.I:
        if c.isdigit():
            next = State.A
        elif c == '.':
            next = State.B
        else:
            next = State.C
    return next


def isNumber(s: str) -> bool:
    state = State.S
    for c in s:
        state = transition(state, c)
        if state == State.C:
            return False
    if state == State.S or state == State.B or state == State.I or state == State.D or state == State.E:
        return False
    return True


def sortUsingComparator(points):
    # compare two points a and b
    def compare(a, b):
        if a[0] != b[0]:
            return a[0]-b[0]
        if a[0] == b[0]:
            return a[1]-b[1]

    points.sort(key=functools.cmp_to_key(compare))
    print(points)


points = [[0, 1], [4, 5], [2, 3], [2, 1], [2, 4]]
sortUsingComparator(points)
