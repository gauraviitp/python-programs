class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.st = [0] * 4 * len(self.nums)
        self.build(1, 0, len(nums)-1)

    def build(self, i, nl, nr):
        st = self.st

        if nl == nr:
            st[i] = self.nums[nl]
        else:
            nm = (nl + nr) // 2
            self.build(i*2, nl, nm)
            self.build(i*2+1, nm+1, nr)

            st[i] = st[i*2] + st[i*2+1]

    def _update(self, i, nl, nr, index, val):
        if nl == nr:
            self.st[i] = val

        else:
            nm = (nl + nr) // 2

            if index <= nm:
                self._update(i*2, nl, nm, index, val)
            else:
                self._update(i*2+1, nm+1, nr, index, val)

            self.st[i] = self.st[i*2] + self.st[i*2+1]

    def update(self, index: int, val: int) -> None:
        self._update(1, 0, len(self.nums)-1, index, val)

    def sum(self, i, nl, nr, left, right):
        if left > right:
            return 0

        if left == nl and right == nr:
            return self.st[i]

        nm = (nl + nr) // 2

        return self.sum(i*2, nl, nm, left, min(nm, right)) + \
            self.sum(i*2+1, nm + 1, nr, max(nm + 1, left), right)

    def sumRange(self, left: int, right: int) -> int:
        return self.sum(1, 0, len(self.nums)-1, left, right)


obj = NumArray([1, 3, 5])
print(obj.sumRange(0, 2))
obj.update(1, 2)
print(obj.sumRange(0, 2))
