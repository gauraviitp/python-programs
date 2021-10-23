class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:

        fx1 = fy1 = math.inf
        fx2 = fy2 = -math.inf

        area = 0

        points = set()

        for rect in rectangles:
            x1, y1 = rect[0], rect[1]
            x2, y2 = rect[2], rect[3]

            area += (x2 - x1) * (y2 - y1)

            for point in [(x1, y1), (x2, y1), (x1, y2), (x2, y2)]:
                if point in points:
                    points.remove(point)
                else:
                    points.add(point)

            fx1 = min(fx1, x1)
            fy1 = min(fy1, y1)
            fx2 = max(fx2, x2)
            fy2 = max(fy2, y2)

        for point in [(fx1, fy1), (fx2, fy1), (fx1, fy2), (fx2, fy2)]:
            if point not in points:
                return False

        return len(points) == 4 and area == (fx2 - fx1) * (fy2 - fy1)
