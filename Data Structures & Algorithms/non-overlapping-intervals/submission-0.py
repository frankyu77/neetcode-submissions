class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        sol = 0
        prev = float('-inf')

        for start, end in intervals:
            if start >= prev:
                prev = end
            else:
                sol += 1

        return sol