class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort()
        stack = [intervals[0]]

        for inval in intervals[1:]:
            if stack[-1][-1] >= inval[0]:
                start, end = stack.pop()
                end = max(end, inval[-1])
                stack.append([start, end])
            else:
                stack.append(inval)
        
        return stack