"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        prev, cur = 0, 1

        while cur < len(intervals):
            prevInterval = intervals[prev]
            interval = intervals[cur]

            if not prevInterval.end <= interval.start:
                return False

            prev += 1
            cur += 1

        return True
