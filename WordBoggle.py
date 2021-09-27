class TrieNode:

    def __init__(self):
        self.char = {}
        self.word = None

    def __getitem__(self, c):
        if c in self.char:
            return self.char[c]
        else:
            return None

    def build(self, words):

        for word in words:
            root = self

            for c in word:
                if c not in root.char:
                    root.char[c] = TrieNode()
                root = root.char[c]

            root.word = word

        return self


class Solution:
    def wordBoggle(self, board, dictionary):
        # return list of words(str) found in the board
        trie = TrieNode().build(dictionary)

        rows, cols = len(board), len(board[0])

        deltax = [-1, 0, 1, -1, 1, -1, 0, 1]
        deltay = [-1, -1, -1, 0, 0, 1, 1, 1]

        res = []

        def dfs(i, j, root):

            c = board[i][j]

            if c == '#':
                return

            if not root[c]:
                return

            if root[c].word:
                res.append(root[c].word)
                root[c].word = None

            board[i][j] = '#'

            for dx, dy in zip(deltax, deltay):
                x = i + dx
                y = j + dy

                if 0 <= x < rows and 0 <= y < cols:
                    if board[x][y] != '#':
                        dfs(x, y, root[c])

            board[i][j] = c

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, trie)

        return sorted(res)


sol = Solution()
res = sol.wordBoggle(
    [
        ['G', 'I', 'Z'],
        ['U', 'E', 'K'],
        ['Q', 'S', 'E']
    ],
    ["GEEKS", "FOR", "QUIZ", "GO"]
)

print(res)
