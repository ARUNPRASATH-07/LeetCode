class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if not intervals:
            return []
        
        intervals.sort()
        
        res = [intervals[0]]
        
        for start, end in intervals[1:]:
            
            last_end = res[-1][1]
            
            if start <= last_end:
                # overlap → merge
                res[-1][1] = max(last_end, end)
            else:
                # no overlap
                res.append([start, end])
        
        return res