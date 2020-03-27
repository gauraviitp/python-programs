from LeetCode import isPossibleDivide
from LeetCode import MedianFinder

def isPossibleDivide_test():
    nums = [1,2,3,4,5,1,2,3,4,5,1,2,3,4]
    assert isPossibleDivide(nums, 5) == False, "Incorrect solution"

    nums = [3,2,1,2,3,4,3,4,5,9,10,11]
    assert isPossibleDivide(nums, 3) == True, "Incorrect solution"

def median_finder_test():
    median_finder = MedianFinder()
    median_finder.addNum(1)
    assert median_finder.findMedian() == 1, "x"
    median_finder.addNum(2)
    assert median_finder.findMedian() == 1.5, "x"
    median_finder.addNum(3)
    assert median_finder.findMedian() == 2, "x"

    median_finder = MedianFinder()
    median_finder.addNum(-1)
    assert median_finder.findMedian() == -1, "x"
    median_finder.addNum(-2)
    assert median_finder.findMedian() == -1.5, "x"
    median_finder.addNum(-3)
    assert median_finder.findMedian() == -2, "x"
    median_finder.addNum(-4)
    assert median_finder.findMedian() == -2.5, "x"
    median_finder.addNum(-5)
    assert median_finder.findMedian() == -3, "x"

def main():
    isPossibleDivide_test()
    median_finder_test()

if __name__ == '__main__':
    main() 