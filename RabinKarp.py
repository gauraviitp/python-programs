# Function to locate the occurrence of the string x in the string s.
def strstr(s, x):
    mod = 10**9 + 7
    p = 257
    p_pow = 1

    # if len(x) == 3, p_pow should be  p**2
    # as when you reach i == 2 you would have multiplied p twice to s[j]
    for i in range(len(x) - 1):
        p_pow = (p_pow*p) % mod

    hx = 0
    for c in x:
        hx = (hx * p + ord(c)) % mod

    hs = 0
    for i in range(len(s)):
        hs = (hs * p + ord(s[i])) % mod

        if i >= len(x)-1:
            j = i - len(x) + 1

            if hs == hx:
                return j

            # subtract the contribution of s[j]
            hs = (hs - p_pow * ord(s[j])) % mod

    return -1


print(strstr('GeeksForGeeks', 'For'))
