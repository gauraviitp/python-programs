
# Extended euclid algorithm to find the solutions
# for equation a * x + b * y = gcd(a, b)
# This method returns gcd(a,b) as well as x and y.
def euclid(a, b, x, y):
    if b == 0:
        x[0] = 1
        y[0] = 0
        return a

    x1 = [0]
    y1 = [0]
    d = euclid(b, a % b, x1, y1)
    x[0] = y1[0]
    y[0] = x1[0] - y1[0] * (a//b)
    return d

# Function to find inverse of a number a modulo m.
# To divide by a modulo m, multiplying with this inverse
# will work fine.


def inverse(a, mod):
    x = [0]
    y = [0]
    g = euclid(a, mod, x, y)
    assert g == 1
    return (x[0] % mod + mod) % mod


# O(n logn) solution using Rabin Karp algorithm
# Times out in geeksforgeeks.
# They are looking for Manachers O(n) solution
def LongestPalindromeSubString(text):
    # code here

    n = len(text)

    def palindrome(k):

        p = 257
        rp = 1
        pPow = p ** (k-1)

        mod = 10**9 + 7

        hash = 0
        rhash = 0

        for i, c in enumerate(text):
            hash = (hash * p + ord(c)) % mod
            rhash = (rhash + ord(c) * rp) % mod

            if i < k - 1:
                rp = (rp * p) % mod

            elif i >= k-1:
                if hash == rhash:
                    return True, i-k+1

                hash = (hash - ord(text[i-k+1]) * pPow) % mod
                rhash = (rhash - ord(text[i-k+1])) % mod
                # since rhash needed to be divided by pPow
                # we will have to multiply by inverse of pPow modulo mod
                rhash = (rhash * inverse(p, mod)) % mod

        return False, -1

    lo = 1
    hi = n

    maxLen = 1
    maxStart = 0

    while lo <= hi:
        mid = (lo + hi) // 2

        # We need to check at mid, mid+1 because
        # we need to check for palindromes of odd length also.

        possibleMid, iMid = palindrome(mid)

        if possibleMid:
            if mid > maxLen:
                maxLen = mid
                maxStart = iMid
            lo = mid + 1
            continue

        possibleMidNext, iMidNext = palindrome(mid+1)

        if possibleMidNext:
            if mid + 1 > maxLen:
                maxLen = mid + 1
                maxStart = iMidNext
            lo = mid + 1
        else:
            hi = mid - 1

    return text[maxStart: maxStart + maxLen]


print(LongestPalindromeSubString('fdjjjjjjjjjjdfdjjjjj'))
