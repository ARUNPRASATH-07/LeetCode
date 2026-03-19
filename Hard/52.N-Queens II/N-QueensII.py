class Solution(object):
    def totalNQueens(self, n):
        
        def backtrack(cols, diag1, diag2):
            
            # All columns filled → found valid solution
            if cols == (1 << n) - 1:
                return 1
            
            count = 0
            
            # Get all available positions
            available = ~(cols | diag1 | diag2) & ((1 << n) - 1)
            
            while available:
                
                # Pick rightmost available position
                position = available & -available
                
                # Remove this position from available
                available -= position
                
                count += backtrack(
                    cols | position,
                    (diag1 | position) << 1,
                    (diag2 | position) >> 1
                )
            
            return count
        
        return backtrack(0, 0, 0)