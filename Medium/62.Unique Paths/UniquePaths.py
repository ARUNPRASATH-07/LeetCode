class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mat=[[0]* n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    mat[i][j]=1
                else:
                    mat[i][j]=mat[i][j-1]+mat[i-1][j]
        return mat[m-1][n-1]