class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # Sort the intervals by their start
        # To achieve removing the least amount of intervals, we should try to remove the largest intervals on overlap
        # When sorted intervals overlap, they either have a partial overlap or one is completely overlapped by the other
        # By doing max(start, interval[0]), min(end, interval[1]), we only 'remove' the larger interval when they overlap completely

        intervals.sort(key=lambda x: x[0])

        start, end = intervals[0]
        overlaps = 0

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if not interval[0] >= end:
                if interval[1] <= end:
                    start, end = max(start, interval[0]), min(end, interval[1])
                overlaps += 1
            else:
                start, end = interval
        
        return overlaps