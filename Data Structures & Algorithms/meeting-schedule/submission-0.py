"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        for i in range(1,len(intervals)):
            #Check n and n-1, start at 1
            if intervals[i].start < intervals[i-1].end:
                return False
        return True
