class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=0
        c=0
        for i in nums:
            if i==1:
                c+=1
                m=max(m,c)
            else:
                c=0
        return m
        