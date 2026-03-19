class Solution(object):
    def subsets(self, nums):
        result = []
        
        def backtrack(start, path):
            # Every path is a subset
            result.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])      # choose
                backtrack(i+1, path)     # explore
                path.pop()               # undo
        
        backtrack(0, [])
        return result