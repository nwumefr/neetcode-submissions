"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        _len = len(intervals)
        si = [(i.start,i.end) for i in intervals]
        si.sort()
        for i in range(_len - 1):
            start = si[i+1][0]
            end = si[i][1]
            print(start,end)
            if start < end:
                return False
        return True
