class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        removals = 0
        last_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < last_end:
                # Overlap: remove the interval that ends later
                removals += 1
                last_end = min(last_end, end)
            else:
                # No overlap
                last_end = end

        return removals