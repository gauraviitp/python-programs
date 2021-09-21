import sys

sys.stdin = open(f'Kickstart\\2020_B_input.txt')
sys.stdout = open(f'Kickstart\\2020_B_open.text', 'w')


def read_ints():
    return map(int, input().split())


def is_possible(minutes, gap, sessions):
    required_sessions = 0

    for i in range(1, len(minutes)):

        required_sessions += (minutes[i] - minutes[i-1] - 1) // gap

        if required_sessions > sessions:
            return False

    return True


def solve_workout():
    t, = read_ints()

    for test_case in range(1, t+1):

        n, k = read_ints()

        minutes = list(read_ints())

        low_gap, high_gap = 1, max(
            minutes[i] - minutes[i-1] for i in range(1, len((minutes))))

        while low_gap < high_gap:

            gap = (low_gap + high_gap) // 2

            if is_possible(minutes, gap, k):
                # try to reduce the gap
                high_gap = gap
            else:
                low_gap = gap + 1

        print(f'Case #{test_case}: {low_gap}')


if __name__ == '__main__':
    solve_workout()
