from LeetCode import isPossibleDivide
from LeetCode import MedianFinder
from LeetCode import maxChunksToSorted
from LeetCode import MinRefuelStops
from LeetCode import LargestDivisibleSubset
from LeetCode import MinSumOfLengths
from LeetCode import MaxVowels
from LeetCode import LongestOnes
from LeetCode import AllPathsSourceTarget
from LeetCode import AlienDictionary
from LeetCode import PalindromePartioningII


def isPossibleDivide_test():
    nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4]
    assert isPossibleDivide(nums, 5) == False, "Incorrect solution"

    nums = [3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11]
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


def max_chunks_to_sorted_ii():
    arr = [5, 4, 3, 2, 1]
    assert maxChunksToSorted(arr) == 1, "x"
    arr = [2, 1, 3, 4, 4]
    assert maxChunksToSorted(arr) == 4, "x"


def minRefuelStops_tests():
    sol = MinRefuelStops()
    assert sol.minRefuelStops(210, 10,  [[10, 100], [110, 0]]), "Test 1"


def largestDivisibleSubset_tests():
    sol = LargestDivisibleSubset()
    assert sol.largestDivisibleSubset([1, 2, 4, 6, 8]) == [
        8, 1, 2, 4], "Test 0"
    assert sol.largestDivisibleSubset([1]) == [1], "Test 1"
    assert sol.largestDivisibleSubset([546, 669]) == [669], "Test 2"


def minSumOfLengths_tests():
    sol = MinSumOfLengths()
    assert sol.minSumOfLengths([7, 3, 4, 7], 7) == 2, "Test 1"
    assert sol.minSumOfLengths(
        [31, 1, 1, 18, 15, 3, 15, 14], 33) == 5, "Test 1"
    assert sol.minSumOfLengths([3, 1, 1, 1, 5, 1, 2, 1], 3) == 3, "Test 0"
    assert sol.minSumOfLengths([3, 2, 2, 4, 3], 3) == 2, "Test 1"


def maxVowels():
    sol = MaxVowels()
    assert sol.maxVowels("abciiidef", 3) == 3, "Failure!"


def longestOnes():
    sol = LongestOnes()
    assert sol.longestOnes(
        [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3) == 10, "x"


def allPathsSourceTarget():
    sol = AllPathsSourceTarget()
    assert sol.allPathsSourceTarget([[1, 2], [3], [3], []]), "x"


def alienDictionary():
    sol = AlienDictionary()
    assert sol.solve(["caa", "aaa", "aab"]) == ['c', 'a', 'b']


def palindromePartioningII():
    sol = PalindromePartioningII()
    assert sol.minCut('abbab') == 1


def main():
    palindromePartioningII()
    alienDictionary()
    allPathsSourceTarget()
    longestOnes()
    maxVowels()
    minSumOfLengths_tests()
    largestDivisibleSubset_tests()
    minRefuelStops_tests()
    isPossibleDivide_test()
    median_finder_test()
    max_chunks_to_sorted_ii()


if __name__ == '__main__':
    main()
