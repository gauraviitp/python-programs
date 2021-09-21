from typing import NamedTuple
from typing import Sequence as List
import heapq


class Result(NamedTuple):
    start: int
    height: int


class Building(NamedTuple):
    negHeight: int
    end: int


class SortedTuple(NamedTuple):
    start: int
    negHeight: int
    end: int


class Solution:

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        # Sort the buildings from the left to right.
        # Taller building should be seen first.
        # Else we will have to write logic to see all the
        # buildings at point x and choose the tallest
        # building at x.
        sortedBuildingEvents = sorted([SortedTuple(start, -height, end) for start, end,
                                       height in buildings] + [SortedTuple(end, 0, end) for _, end, _ in buildings])

        # heap to hold all the live buildings
        heap = []
        result = []

        NoBuilding = Building(negHeight=0, end=0)

        for start, negHeight, end in sortedBuildingEvents:

            # Remove all the buildings that are on the
            # top of the heap and are not live anymore.
            while heap and heap[0].end <= start:
                heapq.heappop(heap)

            # If event is end event (when building cease to exist at a point),
            # skip heappush for such event.
            if start != end:
                heapq.heappush(heap, Building(negHeight=negHeight, end=end))

            # See if a live building is present, else specify no building
            liveBuilding = heap[0] if heap else NoBuilding

            # If height of new live building at point x is different, update the result.
            if not result or result[-1].height != -liveBuilding.negHeight:
                result.append(Result(start, -liveBuilding.negHeight))

        return result


if __name__ == '__main__':
    buildings = [[2, 9, 10], [3, 7, 15], [
        5, 12, 12], [15, 20, 10], [19, 24, 8]]
    solution = Solution().getSkyline(buildings)
