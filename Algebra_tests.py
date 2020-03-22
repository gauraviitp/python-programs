import Algebra

def binary_exponentiation_test():
    assert Algebra.binary_exponentiation(3, 5) == 243, "Not equal to 243"
    assert Algebra.binary_exponentiation(2, 0) == 1, "Not equal to 1"
    assert Algebra.binary_exponentiation(4, 1) == 4, "not equal to 4"

def gcd_test():
    assert Algebra.gcd(4, 2) == 2, "Not equal to 2"
    assert Algebra.gcd(4, 3) == 1, "Not equal to 1"

def main():
    binary_exponentiation_test()
    gcd_test()

if __name__ == '__main__':
    main()