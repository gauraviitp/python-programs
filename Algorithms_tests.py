from Algorithms import isNumber

def isNumber_tests():
    assert isNumber('-1.'), f"Test 1. Expected: true, Actual: {isNumber('-1.')}"
    assert isNumber('1.'), f"Test 2. Expected: true, Actual: {isNumber('1.')}"
    assert isNumber('.-1.') == False, f"Test 3. Expected: false, Actual: {isNumber('.-1.')}"
    assert isNumber('.') == False, f"Test 4. Expected: false, Actual: {isNumber('.')}"
    assert isNumber('.1'), f"Test 5. Expected: true, Actual: {isNumber('.1')}"
    assert isNumber('-+1.') == False, f"Test 6. Expected: false, Actual: {isNumber('-+1.')}"
    assert isNumber('-1.+') == False, f"Test 7. Expected: false, Actual: {isNumber('-1.+')}"
    assert isNumber('e-1.+') == False, f"Test 8. Expected: false, Actual: {isNumber('e-1.+')}"
    assert isNumber('-1.e') == False, f"Test 9. Expected: false, Actual: {isNumber('-1.e')}"
    assert isNumber('4e+') == False, f"Test 10. Expected: false, Actual: {isNumber('4e+')}"

def main():
    isNumber_tests()

if __name__ == '__main__':
    main()