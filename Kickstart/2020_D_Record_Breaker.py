import sys

sys.stdin = open(f'Kickstart\\2020_D_Record_Breaker_input.txt')
sys.stdout = open(f'Kickstart\\2020_D_Record_Breaker_output.txt', 'w')


def read_ints():
    return map(int, input().split())


def solve_record_breaker():

    t, = read_ints()

    for test_case in range(1, t+1):

        n, = read_ints()

        visitors = list(read_ints())

        max_upto_i_minus_one = 0

        record_breaking_days = 0

        for i in range(n):

            if ((i == 0 or visitors[i] > max_upto_i_minus_one)
                    and (i == n-1 or i < n-1 and visitors[i] > visitors[i+1])):
                # record breaking day found
                record_breaking_days += 1

            max_upto_i_minus_one = max(max_upto_i_minus_one, visitors[i])

        print(f'Case #{test_case}: {record_breaking_days}')


if __name__ == '__main__':
    solve_record_breaker()
