import Algebra

def binary_exponentiation_test():
    assert Algebra.binary_exponentiation(3, 5) == 243, "Not equal to 243"
    assert Algebra.binary_exponentiation(2, 0) == 1, "Not equal to 1"
    assert Algebra.binary_exponentiation(4, 1) == 4, "not equal to 4"

def gcd_test():
    assert Algebra.gcd(4, 2) == 2, "Not equal to 2"
    assert Algebra.gcd(4, 3) == 1, "Not equal to 1"

def gcd_extended_test():
    x, y = [0], [0]
    d = Algebra.gcd_extended(4, 2, x, y)
    assert d == 2 and x[0] == 0 and y[0] == 1, "Incorrect solution"

def linear_diophantine_equation_test():
    x, y, g = [0], [0], [0]
    f = Algebra.linear_diophantine_equation_any_solution(4, 2, 8, x, y, g)
    assert f and x[0] == 0 and y[0] == 4 and g[0] == 2, "Incorrect solution"

def nth_fibonacci_test():
    assert Algebra.nth_fibonacci(3)[0] == 2, "Incorrect solution"
    assert Algebra.nth_fibonacci(4)[0] == 3, "Incorrect solution"
    assert Algebra.nth_fibonacci(5)[0] == 5, "Incorrect solution"

def main():
    binary_exponentiation_test()
    gcd_test()
    gcd_extended_test()
    linear_diophantine_equation_test()
    nth_fibonacci_test()

if __name__ == '__main__':
    main()