class Solution(object):
    def combine(self, n, k):
        result = []
        
        def backtrack(start, path):
            
            # If combination complete
            if len(path) == k:
                result.append(path[:])
                return
            
            # Try next numbers
            for num in range(start, n+1):
                path.append(num)           # choose
                backtrack(num+1, path)    # explore
                path.pop()                # undo
        
        backtrack(1, [])
        return result