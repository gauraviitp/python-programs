from DataStructures import FenwickTree
from DataStructures import FenwickTreeMin
from DataStructures import FenwickTree2D
from DataStructures import FenwickTree2DMin
import operator

def fenwicktree_test():
    a = [1, 2, 3, 4, 5]
    # operation sum
    bit = FenwickTree.from_list(a, operator.add)
    assert bit.get_range(0, 4) == 15, "Sum from 1 to 5 must be 15"
    bit.update(0, 1)
    assert bit.get_range(1, 4) == 14, "Sum from 2 to 5 must be 14"
    assert bit.get(4) == 16, "Incorrect solution"
    # operation min
    bit = FenwickTreeMin.from_list(a, min)
    assert bit.get(4) == 1, "Min must be 1"
    assert bit.get(3) == 1, "Min must be 1"
    bit.update(2, 0)
    assert bit.get(3) == 0, "Min must be 0"

def fenwicktree2d_test():
    a = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10]
        ]
    bit = FenwickTree2D.from_list(a)
    assert bit.get(1, 1) == 16, "Incorrect solution"
    assert bit.get(1, 2) == 27, "Incorrect solution"

def main():
    fenwicktree_test()
    fenwicktree2d_test()

if __name__ == '__main__':
    main()