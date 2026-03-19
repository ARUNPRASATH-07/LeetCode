class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        return [nums[i//2] if i % 2 == 0 else nums[n + i//2] for i in range(2*n)]
            
            
        