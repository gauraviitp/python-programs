from collections import Counter


class Solution:
    def numMagicSquaresInside(self, grid) -> int:

        rows, cols = len(grid), len(grid[0])

        if rows < 3 or cols < 3:
            return False

        counter = Counter([i for i in range(1, 10)])

        def validate(row, col):

            count = Counter(grid[i][j] for i in range(row, row+3)
                            for j in range(col, col+3))

            if count != counter:
                return False

            rows_sums = [sum(grid[i][col:col+3]) for i in range(row, row+3)]

            if any(x != 15 for x in rows_sums):
                return False

            cols_sums = [sum(grid[i][j] for i in range(row, row+3))
                         for j in range(col, col+3)]

            if any(x != 15 for x in cols_sums):
                return False

            diag_sum = sum(grid[row+i][col+i] for i in range(3))

            if diag_sum != 15:
                return False

            cross_diag_sums = sum(grid[row+2-i][col+i] for i in range(3))

            if cross_diag_sums != 15:
                return False

            return True

        res = 0

        for i in range(rows-2):
            for j in range(cols-2):
                if validate(i, j):
                    res += 1

        return res


grid = [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]

sol = Solution()
print(sol.numMagicSquaresInside(grid))
