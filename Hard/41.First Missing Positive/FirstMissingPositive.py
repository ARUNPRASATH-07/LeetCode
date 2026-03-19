class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        seen = set(nums)
        i=1
        while i in seen:
            i += 1
        return i