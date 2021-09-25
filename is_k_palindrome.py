from functools import lru_cache


def is_k_palin(string, n):

    @lru_cache(None)
    def recurse(i, j, k):
        if i >= j:
            return True

        if string[i] == string[j]:
            return recurse(i+1, j-1, k)
        elif k > 0:
            return recurse(i+1, j, k-1) or recurse(i, j-1, k-1)

        return False

    return int(recurse(0, len(string)-1, n))


print(is_k_palin('abcdecba', 1))
print(is_k_palin('acdcb', 1))
