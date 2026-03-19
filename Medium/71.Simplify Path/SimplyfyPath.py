class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack=[]
        path=path.split("/")

        for i in path:
            if i=="..":
                if  stack:
                    stack.pop()
                    
            elif i=="." or i=="":
                continue
            else:
                stack.append(i)
        return "/"+ "/".join(stack)

    
        class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0]*n for _ in range(m)]
        
        dp[0][0] = grid[0][0]
        
        # First row
        for j in range(1, n):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        
        # First column
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        
        # Rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[m-1][n-1]