class Solution(object):
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        
        def dfs(i, j, index):
            
            # word fully matched
            if index == len(word):
                return True
            
            # boundary / mismatch check
            if (i < 0 or i >= m or 
                j < 0 or j >= n or 
                board[i][j] != word[index]):
                return False
            
            temp = board[i][j]
            board[i][j] = "#"   # mark visited
            
            # explore 4 directions
            found = (dfs(i+1, j, index+1) or
                     dfs(i-1, j, index+1) or
                     dfs(i, j+1, index+1) or
                     dfs(i, j-1, index+1))
            
            board[i][j] = temp  # restore (backtrack)
            
            return found
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False