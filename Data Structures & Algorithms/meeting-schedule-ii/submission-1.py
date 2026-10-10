"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        end_heap = []
        count = 0
        
        for i in intervals:
            while end_heap and end_heap[0] <= i.start:
                heapq.heappop(end_heap)
            heapq.heappush(end_heap, i.end)
            count = max(count, len(end_heap))
        return count