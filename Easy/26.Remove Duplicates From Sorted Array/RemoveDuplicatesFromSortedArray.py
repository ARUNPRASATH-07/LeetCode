class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0  # position to place next unique element
        
        for num in nums:
            if k == 0 or num != nums[k - 1]:
                nums[k] = num
                k += 1
                
        return k
        