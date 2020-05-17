import Strings

def prefix_function_tests():
    assert Strings.prefix_function('abcabcd') == [0, 0, 0, 1, 2, 3, 0], "wrong prefix"

def kmp_tests():
    assert Strings.kmp('abcabcd', 'abcabcdabcabcdabcabcd') == [0, 7, 14], Strings.kmp('abcabcd', 'abcabcdabcabcdabcabcd')
    assert Strings.kmp('abcabc', 'abcabcabcabcdabcabcd') == [0, 3, 6, 13], Strings.kmp('abcabc', 'abcabcabcabcdabcabcd')
    assert Strings.kmp('AABA', 'AABAACAADAABAABA') == [0, 9, 12], Strings.kmp('AABA', 'AABAACAADAABAABA')
    assert Strings.kmp('AAA', 'AAAAA') == [0, 1, 2], Strings.kmp('AAA', 'AAAAA')

def main():
    prefix_function_tests()
    kmp_tests()

if __name__ == '__main__':
    main()