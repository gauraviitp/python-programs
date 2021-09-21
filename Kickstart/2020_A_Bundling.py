import sys

sys.stdin = open(f'Kickstart\\2020_C_input.txt')
sys.stdout = open(f'Kickstart\\2020_C_output.txt', 'w')

sys.setrecursionlimit(10**6)


class TrieNode:

    def __init__(self):

        self.next = {}
        self.count = 0


class Trie:

    def __init__(self):

        # initialize with a dummy node
        self.root = TrieNode()

    def add_word(self, word):

        root = self.root

        for char in word:

            if char not in root.next:
                root.next[char] = TrieNode()

            root.next[char].count += 1

            root = root.next[char]

    def get_recurse(self, k, root):

        res = 0

        for char in root.next:

            res += root.next[char].count // k
            res += self.get_recurse(k, root.next[char])

        return res

    def get(self, k):

        return self.get_recurse(k, self.root)


def read_ints():
    return map(int, input().split())


def solve_bundling():

    t, = read_ints()

    for test_case in range(1, t + 1):

        n, k = read_ints()

        trie = Trie()

        for _ in range(n):

            # add the word to the trie
            trie.add_word(input())

        print(f'Case #{ test_case }: { trie.get(k) }')


if __name__ == '__main__':
    solve_bundling()
