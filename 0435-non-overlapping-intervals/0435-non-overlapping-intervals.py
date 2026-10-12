class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        end=float('-inf')
        removed=0
        for start,finish in intervals:
            if start<end:
                removed+=1
            else:
                end=finish
        return removed