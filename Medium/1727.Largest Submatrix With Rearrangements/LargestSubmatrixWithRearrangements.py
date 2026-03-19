class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        height = [0] * cols
        max_area = 0
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    height[j] += 1
                else:
                    height[j] = 0
            temp = height[:]
            temp.sort(reverse=True)
            for k in range(cols):
                if temp[k] == 0:
                    break
                area = temp[k] * (k + 1)
                if area > max_area:
                    max_area = area
        return max_area