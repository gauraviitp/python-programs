import random
import math
from matplotlib import pyplot


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):

        while True:
            # get random x
            x = random.uniform(self.x_center - self.radius,
                               self.x_center + self.radius)

            # get random y
            y = random.uniform(self.y_center - self.radius,
                               self.y_center + self.radius)

            if (x - self.x_center) ** 2 + (y - self.y_center) ** 2 <= self.radius ** 2:
                return [x, y]


obj = Solution(1, 0, 0)
x_points = []
y_points = []
for _ in range(2000):
    x, y = obj.randPoint()
    x_points.append(x)
    y_points.append(y)

pyplot.plot(x_points, y_points, "ro")
pyplot.savefig("plot2.png")
