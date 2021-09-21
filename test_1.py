import sys
import collections
import math
import itertools
import random

from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(2 * 10**6)

sys.stdin = open(f'input.txt')
sys.stdout = open(f'output.txt', 'w')


def read():
    return list(map(int, input().split()))


def average():

    res = 0

    for _ in range(100000):

        skill_level = random.uniform(-3, 3)
        diff_level = random.uniform(-3, 3)

        res += 1 / (1 + math.exp(- skill_level + diff_level))

    return res / 100000


def solve():
    t, = read()
    p, = read()

    for testCase in range(1, t+1):

        #avg = average()

        res = []

        questions = [0] * (10001)

        players = [[]]

        for i in range(1, 101):
            player_ans = input()

            for i, ans in enumerate(player_ans):

                if ans == '1':
                    questions[i+1] += 1

            players.append(player_ans)

        player_scores = [0] * (101)

        sorted_questions = list(
            sorted([(i, questions[i]) for i in range(1, 10001)], key=lambda x: x[1]))

        for question_no, score in sorted_questions:

            for player_no in range(1, 101):

                if players[player_no][question_no-1] == '1':
                    #player_scores[player_no] += 1 - score/100
                    player_scores[player_no] += 1 / \
                        (1 + math.exp(-(1 - score/100) * 4))

        sorted_players = list(
            sorted([(i, player_scores[i]) for i in range(1, 101)], key=lambda x: -x[1]))

        print(f'Case #{testCase}: {sorted_players[0][0]}')


solve()
