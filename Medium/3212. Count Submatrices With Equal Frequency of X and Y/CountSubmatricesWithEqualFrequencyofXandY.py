class Solution:
    def numberOfSubmatrices(self, grid):
        r, c = len(grid), len(grid[0])
        
        # prefix sums
        px = [[0]*(c+1) for _ in range(r+1)]
        py = [[0]*(c+1) for _ in range(r+1)]
        
        # build prefix
        for i in range(r):
            for j in range(c):
                px[i+1][j+1] = px[i][j+1] + px[i+1][j] - px[i][j] + (grid[i][j] == 'X')
                py[i+1][j+1] = py[i][j+1] + py[i+1][j] - py[i][j] + (grid[i][j] == 'Y')
        
        res = 0
        
        # check all (0,0) → (i,j)
        for i in range(r):
            for j in range(c):
                x = px[i+1][j+1]
                y = py[i+1][j+1]
                
                if x == y and x > 0:
                    res += 1
        
        return res