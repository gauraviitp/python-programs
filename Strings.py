""" prefix function
    Given a string s[0...n-1], prefix function pi[0...n-1] where pi[i] is defined
    as the largest length of the largest proper suffix (not matching the entire string) 
    of substring s[0...i] that matches its prefix.
    pi[0] assumed to be zero and 
    pi[i] = max over k = 0...i {k: s[0...k-1] = s[i-k+1...i]}
"""
def prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i-1]
        while j > 0 and s[j] != s[i]: j = pi[j-1]
        if s[i] == s[j]: j += 1
        pi[i] = j
    return pi

"""
    Returns all occurences of s in text.
"""
def kmp(s, text):
    pi = prefix_function(s)
    n, m = len(s), len(text)
    i, j = 0, 0
    res = []
    while i < m:
        while j > 0 and s[j] != text[i]: j = pi[j-1]
        if text[i] == s[j]: j += 1
        if j == n:
            res.append(i-j+1)
            j = pi[n-1]
        i += 1
    return res